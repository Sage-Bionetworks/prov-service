import logging

from random import randrange, sample
from py2neo import Graph, NodeMatcher

from synprov.config import neomod
from synprov.mockup_data.activity import MockActivity
from synprov.mockup_data.agent import MockAgent
from synprov.mockup_data.reference import MockReference
from synprov.mockup_data.relationship import MockRelationship
from synprov.mockup_data.dict import ReferenceSubclasses, ActivityRoles


logger = logging.getLogger(__name__)
graph = Graph(neomod.neo.db.url)
matcher = NodeMatcher(graph)


class ActivityMocker:
    def __init__(self, graph_db, activity, ref_num=0, agt_num=0, ref_limit=2):
        self.gdb = graph_db
        self.activity = activity
        activity_subclasses = ActivityRoles[self.activity._class]
        self.in_subclasses = activity_subclasses['in_subclass']
        self.out_subclasses = activity_subclasses['out_subclass']
        self.ref_num = self.count_refs() + 1
        self.agt_num = self.count_agts() + 1
        self.used_refs = self.add_used(limit=randrange(ref_limit)+1)
        self.used_rels = self.connect_used()
        self.agts = self.add_agents()
        self.associated_rels = self.connect_associated()
        self.generated_refs = self.add_generated(limit=randrange(ref_limit-1)+1)
        self.generated_rels = self.connect_generated()
        self.attributed_rels = self.connect_attributed()

    def __repr__(self):
        rels = []
        for r in self.used_rels:
            rels.append("\t({a})[{ac}] — [:USED]{{start_role: '{s}', end_role: '{e}'}} —> ({r})"
                        .format(a=self.activity.name,
                                ac=self.activity._class,
                                s=r.start_node_role,
                                e=r.end_node_role,
                                r=['({})[{}]'.format(
                                    u.name, u.subclass)
                                    for u in self.used_refs
                                   if u.id == r.end_node][0]))
        for r in self.associated_rels:
            rels.append("\t({a})[{ac}] — [:WASASSOCIATEDWITH]{{start_role: '{s}', end_role: '{e}'}} —> ({t})"
                        .format(a=self.activity.name,
                                ac=self.activity._class,
                                s=r.start_node_role,
                                e=r.end_node_role,
                                t=['({})'.format(
                                    a.name)
                                   for a in self.agts
                                   if a.id == r.end_node][0]))
        for r in self.generated_rels:
            rels.append("\t({r}) — [:WASGENERATEDBY]{{start_role: '{s}', end_role: '{e}'}} —> ({a})[{ac}]"
                        .format(a=self.activity.name,
                                ac=self.activity._class,
                                s=r.start_node_role,
                                e=r.end_node_role,
                                r=['({})[{}]'.format(
                                    g.name, g.subclass)
                                   for g in self.generated_refs
                                   if g.id == r.start_node][0]))
        for r in self.attributed_rels:
            rels.append("\t({r}) — [:WASATTRIBUTEDTO]{{start_role: '{s}', end_role: '{e}'}} —> ({t}]"
                        .format(r=['({})[{}]'.format(
                                    g.name, g.subclass)
                                    for g in self.generated_refs
                                   if g.id == r.start_node][0],
                                s=r.start_node_role,
                                e=r.end_node_role,
                                t=['({})'.format(
                                    a.name)
                                   for a in self.agts
                                   if a.id == r.end_node][0]))
        return '\n'.join(rels)

    def count_refs(self):
        result = self.gdb.graph.run(
            '''
            MATCH (:Reference)
            RETURN count(*) as count
            '''
        )
        return result.data()[0]['count']

    def count_agts(self):
        result = self.gdb.graph.run(
            '''
            MATCH (:Agent)
            RETURN count(*) as count
            '''
        )
        return result.data()[0]['count']

    def add_used(self, limit=3):
        used_refs_data = _unpack_subclass_roles(self.in_subclasses,
                                                'USED')
        used_refs_data = _expand_roles_data(used_refs_data)
        if len(used_refs_data) > limit:
            used_refs_data = sample(used_refs_data, limit)
        offset = max(self.ref_num, 1)
        refs = _add_references(used_refs_data, offset=offset)
        self.ref_num = self.ref_num + len(used_refs_data)
        return refs

    def connect_used(self):
        logger.debug("Generating :USED records")
        used_rels = [MockRelationship(self.activity, ref)
                     for ref in self.used_refs]
        return used_rels

    def add_agents(self, limit=1):
        agts_data = _unpack_subclass_roles(self.in_subclasses,
                                           'WASASSOCIATEDWITH')
        agts_data = _expand_roles_data(agts_data)
        agts = _add_agents(agts_data, offset=self.agt_num)
        self.agt_num = self.agt_num + len(agts_data)
        return agts

    def connect_associated(self):
        logger.debug("Generating :WASASSOCIATEDWITH records")
        associated_rels = [MockRelationship(self.activity, agt)
                           for agt in self.agts]
        return associated_rels

    def add_generated(self, limit=3):
        generated_refs_data = _unpack_subclass_roles(self.out_subclasses,
                                                     'WASGENERATEDBY')
        generated_refs_data = _expand_roles_data(generated_refs_data)
        if len(generated_refs_data) > limit:
            generated_refs_data = sample(generated_refs_data, limit)
        refs = _add_references(generated_refs_data,
                               offset=self.ref_num,
                               exists=False)
        self.ref_num = self.ref_num + len(generated_refs_data)
        return refs


    def connect_generated(self):
        logger.debug("Generating :WASGENERATEDBY records")
        generated_rels = [MockRelationship(gen, self.activity)
                          for gen in self.generated_refs]
        return generated_rels

    def connect_attributed(self):
        logger.debug("Generating :WASATTRIBUTEDTO records")
        attributed_rels = [MockRelationship(gen, agt, self.activity._class)
                          for gen in self.generated_refs
                          for agt in self.agts]
        return attributed_rels

    def save(self):
        self.gdb.create_node(self.activity)
        for u in self.used_refs:
            self.gdb.create_node(u)
        for ur in self.used_rels:
            self.gdb.create_relationship(ur)
        for g in self.generated_refs:
            self.gdb.create_node(g)
        for gr in self.generated_rels:
            self.gdb.create_relationship(gr)
        for a in self.agts:
            self.gdb.create_node(a)
        for ar in self.associated_rels:
            self.gdb.create_relationship(ar)
        for ar in self.attributed_rels:
            self.gdb.create_relationship(ar)
        logging.info("Activity relationships:\n{}".format(self.__repr__()))
        return (self.ref_num, self.agt_num)


class MockFactory:
    def __init__(self, type, **kwargs):
        mock_types = {
            'Reference': MockReference,
            'Agent': MockAgent,
        }
        self.obj = mock_types[type](**kwargs)

    def create(self):
        return self.obj


def _unpack_subclass_roles(subclass_array, relationship_type):
    parts = [(sc, sci['role'], randrange(sci['num'][0], sci['num'][1]+1))
                for sc, sci in subclass_array[relationship_type].items()]
    return parts


def _expand_roles_data(roles_data):
    return [r[0:2]*r[2] for r in roles_data if r[2]]


def _node_to_object(node, mock_type):
    mock_data = dict(node)
    mock_data.update({
        'label': list(node.labels)[0]
    })
    mock_object = MockFactory(mock_type, **mock_data).create()
    return mock_object


def _create_agent(agt, idx, offset):
    mock_agt = MockAgent(name='User_' + str(idx + offset),
                         user_id='UserID_' + str(idx + offset))
    logging.debug("agt created: {}".format(mock_agt))
    return mock_agt


def _fetch_agent(agt):
    logging.debug("fetching existing Agent node")
    # TODO: any way to make less deterministic than 'first()'?
    agt_nodes = matcher.match(
        'Agent',
    )
    agt_node = agt_nodes.skip(randrange(len(agt_nodes))).first()
    return _node_to_object(agt_node, 'Agent')


def _add_agents(agents, offset=0, exists=None):
    agts = []
    for idx, agt in enumerate(agents):
        if exists is None:
            exists = randrange(2)
        exists = randrange(2)
        if exists:
            try:
                tmp = _fetch_agent(agt)
            except:
                logging.debug("failed; creating new")
                tmp = _create_agent(agt, idx, offset)
        else:
            logging.debug("creating new agent")
            tmp = _create_agent(agt, idx, offset)
        agts.append(tmp)
    return(agts)


def _create_reference(ref, idx, offset):
    mock_ref = MockReference(name='Reference_' + str(idx + offset),
                             target_id='TargetID_' + str(idx + offset),
                             target_version_id='1.0')
    mock_ref.subclass = ref[0]
    mock_ref._class = [c for c in ReferenceSubclasses
                       if ref[0] in ReferenceSubclasses[c]][0]
    logging.debug("ref created: {}".format(mock_ref))
    return mock_ref


def _fetch_reference(ref):
    logging.debug("fetching existing Reference node")
    # TODO: any way to make less deterministic than 'first()'?
    ref_nodes = matcher.match(
        'Reference',
        subclass=ref[0]
    )
    ref_node = ref_nodes.skip(randrange(len(ref_nodes))).first()
    return _node_to_object(ref_node, 'Reference')


def _add_references(references, offset=0, exists=None):
    refs = []
    for idx, ref in enumerate(references):
        if exists is None:
            exists = randrange(2)
        if exists:
            try:
                tmp = _fetch_reference(ref)
            except:
                logging.debug("failed; creating new")
                tmp = _create_reference(ref, idx, offset)
        else:
            logging.debug("creating new reference")
            tmp = _create_reference(ref, idx, offset)
        refs.append(tmp)
    return refs