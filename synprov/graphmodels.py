from uuid import uuid4

from py2neo import Graph, Node, Relationship, NodeMatcher

from synprov.config import neomod


graph = Graph(neomod.neo.db.url)


USED = Relationship.type('USED')
WASGENERATEDBY = Relationship.type('WASGENERATEDBY')
WASATTRIBUTEDTO = Relationship.type('WASATTRIBUTEDTO')
WASASSOCIATEDWITH = Relationship.type('WASASSOCIATEDWITH')


class Activity:
    matcher = NodeMatcher(graph)

    def __init__(self,
                 activity_id=None,
                 id='',
                 name='',
                 description='',
                 used=[],
                 generated=[],
                 agents=[]):

        self.activity_id = activity_id

        self.name = name
        self.description = description

        self.used = used
        self.generated = generated
        self.agents = agents

        self.node = self._find()

    def _find_by_used(self, used):
        activities = graph.run(
            '''
            WITH {u_ids} as refs
            MATCH (r:Reference)<-[:USED]-(act:Activity)
            WHERE r.target_id in refs
            WITH act, size(refs) as inputCnt, count(DISTINCT r) as cnt
            WHERE cnt = inputCnt
            RETURN act
            ''',
            u_ids=[u['target_id'] for u in used]
        ).data()

        if len(activities) > 0:
            return [a['act'] for a in activities]

    def _find_by_agents(self, agents):
        activities = graph.run(
            '''
            WITH {a_ids} as agts
            MATCH (a:Agent)<-[:WASASSOCIATEDWITH]-(act:Activity)
            WHERE a.agent_id in agts
            WITH act, size(agts) as inputCnt, count(DISTINCT a) as cnt
            WHERE cnt = inputCnt
            RETURN act
            ''',
            a_ids=[a['agent_id'] for a in agents]
        ).data()

        if len(activities):
            return [a['act'] for a in activities]

    def _find(self):
        if self.activity_id:
            node = self.matcher.match(
                'Activity',
                activity_id={self.activity_id}
            ).first()
            return node
        elif len(self.used) and len(self.agents):
            used_node = self._find_by_used(self.used)
            agents_node = self._find_by_agents(self.agents)
            if used_node == agents_node and used_node:
                return used_node

    def save(self):
        if not self.node:
            self.activity_id = str(uuid4())

            activity = Node('Activity',
                             activity_id=self.activity_id,
                             name=self.name,
                             description=self.description)
            graph.create(activity)
            self.node = activity

            if len(self.used):
                for u in self.used:
                    self.add_used(u['target_id'], u['target_version_id'])

            if len(self.generated):
                for g in self.generated:
                    self.add_generated(g['target_id'], g['target_version_id'])

            if len(self.agents):
                for a in self.agents:
                    self.add_agent(a['agent_id'])

        return True

    def add_used(self, target_id, target_version_id):
        ref = Reference(
            target_id=target_id,
            target_version_id=target_version_id
        )
        if not ref.node:
            ref.save()
        graph.merge(USED(self.node, ref.node))

    def add_generated(self, target_id, target_version_id):
        ref = Reference(
            target_id=target_id,
            target_version_id=target_version_id
        )
        if not ref.node:
            ref.save()
        graph.merge(WASGENERATEDBY(ref.node, self.node))

    def add_agent(self, agent_id):
        agt = Agent(
            agent_id=agent_id
        )
        if not agt.node:
            agt.save()
        graph.merge(WASASSOCIATEDWITH(self.node, agt.node))


class Reference:
    matcher = NodeMatcher(graph)

    def __init__(self, target_id, target_version_id):
        self.target_id = target_id
        self.target_version_id = target_version_id
        self.node = self._find()

    def _find(self):
        node = self.matcher.match(
            'Reference',
            target_id={self.target_id},
            target_version_id={self.target_version_id}
        ).first()
        return node

    def save(self):
        if not self.node:
            ref = Node('Reference',
                       target_id=self.target_id,
                       target_version_id=self.target_version_id)
            graph.create(ref)
            self.node = ref
        return True


class Agent:
    matcher = NodeMatcher(graph)

    def __init__(self, agent_id, role=''):
        self.agent_id = agent_id
        self.role = role
        self.node = self._find()

    def _find(self):
        node = self.matcher.match(
            'Agent',
            agent_id={self.agent_id}
        ).first()
        return node

    def save(self):
        if not self.node:
            agt = Node('Agent',
                       agent_id=self.agent_id)
            graph.create(agt)
            self.node = agt
        return True

    def add_agent(self, agent_id):
        agt = Agent(
            agent_id=agent_id
        )
        if not agt.node:
            agt.save()
        graph.merge(WASATTRIBUTEDTO(self.node, agt.node))