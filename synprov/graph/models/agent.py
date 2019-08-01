import logging

import uuid

from synprov.models.agent import Agent
from synprov.util import get_datetime

logger = logging.getLogger(__name__)


class GraphAgent(Agent):

    def __init__(self,
                 name='',
                 user_id='',
                 **kwargs):
        super().__init__(name=name, user_id=user_id)
        for kw in kwargs:
            self.__setattr__(kw, kwargs[kw])
        self.label = 'Agent'
        self.openapi_types.update({'label': str})

    def _find_node(self, graph, label, properties):
        return graph.nodes.match(label, **properties).first()

    def create(self, graph):
        logger.debug('Attempting to create node [{}] with properties: {}'
            .format(self.label, self.__dict__))
        node = self._find_node(
            graph,
            self.label,
            {'user_id': self.user_id}
        )
        if not node:
            self.id = str(uuid.uuid1())
            self.created_at = get_datetime()
        else:
            logger.debug("found node: {}".format(node))
            node_data = dict(node)
            self.id = dict(node_data)['id']
            self.created_at = dict(node_data)['created_at']
