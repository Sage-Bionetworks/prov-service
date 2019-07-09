import logging

from random import randrange, sample

from synprov.mockup_data.activity import MockActivity
from synprov.mockup_data.agent import MockAgent
from synprov.mockup_data.reference import MockReference
from synprov.mockup_data.relationship import MockRelationship
from synprov.mockup_data.dict import ActivityRoles


logger = logging.getLogger(__name__)


class ActivityMocker:
    def __init__(self, graph_db, activity, ref_num=0, agt_num=0, ref_limit=3):
        self.gdb = graph_db
        self.activity = activity
        activity_subclasses = ActivityRoles[self.activity._class]
        self.in_subclasses = activity_subclasses['in_subclass']
        self.out_subclasses = activity_subclasses['out_subclass']
        self.ref_num = ref_num
        self.agt_num = agt_num
        self.used_refs = self.add_used(limit=ref_limit)
        self.used_rels = self.connect_used()
        self.agts = self.add_agents()
        self.associated_rels = self.connect_associated()
        self.generated_refs = self.add_generated(limit=ref_limit)
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

    def add_used(self, limit=3):
        used_refs_data = _unpack_subclass_roles(self.in_subclasses,
                                                'USED')
        used_refs_data = _expand_roles_data(used_refs_data)
        if len(used_refs_data) > limit:
            used_refs_data = sample(used_refs_data, limit)
        self.ref_num = self.ref_num + len(used_refs_data)
        return _add_references(used_refs_data, offset=self.ref_num)

    def connect_used(self):
        logger.debug("Generating :USED records")
        used_rels = [MockRelationship(self.activity, ref)
                     for ref in self.used_refs]
        return used_rels

    def add_agents(self, limit=1):
        agts_data = _unpack_subclass_roles(self.in_subclasses,
                                           'WASASSOCIATEDWITH')
        agts_data = _expand_roles_data(agts_data)
        self.agt_num = self.agt_num + len(agts_data)
        return _add_agents(agts_data, offset=self.agt_num)

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
        self.ref_num = self.ref_num + len(generated_refs_data)
        return _add_references(generated_refs_data,
                               offset=self.ref_num)

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
        # self.gdb.createActivityNode(self.activity)
        # for u in self.used_refs:
        #     self.gdb.createReferenceNode(u)
        # for ur in self.used_rels:
        #     self.gdb.createRelationshipUsed(ur)
        # for g in self.generated_refs:
        #     self.gdb.createReferenceNode(g)
        # for gr in self.generated_rels:
        #     self.gdb.createRelationshipGenerated(gr)
        # for a in self.agts:
        #     self.gdb.createAgentNode(a)
        # for ar in self.associated_rels:
        #     self.gdb.createRelationshipAssociated(ar)
        # for ar in self.attributed_rels:
        #     self.gdb.createRelationshipAttributed(ar)
        print(self.__repr__())
        return (self.ref_num, self.agt_num)


def _unpack_subclass_roles(subclass_array, relationship_type):
    parts = [(sc, sci['role'], randrange(sci['num'][0], sci['num'][1]+1))
                for sc, sci in subclass_array[relationship_type].items()]
    return parts


def _expand_roles_data(roles_data):
    return [r[0:2]*r[2] for r in roles_data if r[2]]


def _add_agents(agents, offset=0):
    agts = []
    for idx, agt in enumerate(agents):
        tmp = MockAgent(name='User_' + str(idx + offset + 1),
                        user_id='UserID_' + str(idx + offset + 1))
        agts.append(tmp)
    return(agts)


def _add_references(references, offset=0):
    refs = []
    for idx, ref in enumerate(references):
        tmp = MockReference(name='Reference_' + str(idx + offset + 1),
                            target_id='TargetID_' + str(idx + offset + 1),
                            target_version_id='1.0')
        tmp.subclass = ref[0]
        refs.append(tmp)
    return refs