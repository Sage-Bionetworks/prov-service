import logging
import pytest

from synprov.models import ActivityForm
from synprov.graph.controllers import activities_controller


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestActivitiesController:

    def test_create_activity_exists(self,
                                    mock_graph_data,
                                    mock_activity_request):
        node_count = len(mock_graph_data.nodes)
        rel_count = len(mock_graph_data.relationships)
        body = ActivityForm.from_dict(mock_activity_request)
        act_node = activities_controller.create_activity(body)
        assert len(mock_graph_data.nodes) == node_count
        assert len(mock_graph_data.relationships) == rel_count
        assert all([key in act_node for key in ['id', 'labels', 'properties']])

    def test_create_activity_new(self,
                                 mock_graph,
                                 mock_activity_request):
        node_count = len(mock_graph.nodes)
        rel_count = len(mock_graph.relationships)
        body = ActivityForm.from_dict(mock_activity_request)
        act_node = activities_controller.create_activity(body)

        new_nodes = sum([
            len(mock_activity_request['used']),
            len(mock_activity_request['generated']),
            len(mock_activity_request['agents']),
            1
        ])
        new_rels = sum([
            len(mock_activity_request['used']),
            len(mock_activity_request['generated']),
            len(mock_activity_request['agents']) * 2,
        ])

        assert len(mock_graph.nodes) == (node_count + new_nodes)
        assert len(mock_graph.relationships) == (rel_count + new_rels)
        assert all([key in act_node for key in ['id', 'labels', 'properties']])
