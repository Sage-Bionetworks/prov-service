import logging
import pytest

from synprov.graph.models.activity import GraphActivity
from synprov.graph.models.reference import GraphReference
from synprov.graph.models.agent import GraphAgent
from synprov.graph.builder import ActivityBuilder


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestActivityBuilder:

    def test_init(self, mock_graph, mock_activity_form):
        builder = ActivityBuilder(
            **mock_activity_form
        )
        assert type(builder.activity) is GraphActivity
        assert type(builder.used[0]) is GraphReference
        assert type(builder.generated[0]) is GraphReference
        assert type(builder.agents[0]) is GraphAgent

    def test__find_activity(self, mock_graph_data, mock_activity_form):
        builder = ActivityBuilder(
            **mock_activity_form
        )
        activity = builder._find_activity()
        assert dict(activity)['name'] == mock_activity_form['name']

    def test_save_exists(self, mock_graph_data, mock_activity_form):
        node_count = len(mock_graph_data.nodes)
        rel_count = len(mock_graph_data.relationships)
        builder = ActivityBuilder(
            **mock_activity_form
        )
        activity_id = builder.activity.id
        builder.save()
        assert len(mock_graph_data.nodes) == node_count
        assert len(mock_graph_data.relationships) == rel_count
        assert builder.activity.id == activity_id

    def test_save_similar(self, mock_graph_data, mock_activity_form):
        mock_activity_form['generated'] = [
            {
                'name': 'Reference_X',
                'target_id': 'TargetID_X',
                'target_version_id': '1.0',
                '_class': 'Resource',
                'subclass': 'State'
            }
    ]
        node_count = len(mock_graph_data.nodes)
        rel_count = len(mock_graph_data.relationships)
        builder = ActivityBuilder(
            **mock_activity_form
        )
        activity_id = builder.activity.id
        builder.save()
        new_rels = sum([
            len(mock_activity_form['used']),
            len(mock_activity_form['generated']),
            len(mock_activity_form['agents']) * 2,
        ])
        assert len(mock_graph_data.nodes) == node_count + 2
        assert len(mock_graph_data.relationships) == (rel_count + new_rels)
        assert builder.activity.id != activity_id

    def test_save_new(self, mock_graph, mock_activity_form):
        node_count = len(mock_graph.nodes)
        rel_count = len(mock_graph.relationships)
        builder = ActivityBuilder(
            **mock_activity_form
        )
        activity_id = builder.activity.id
        builder.save()
        new_nodes = sum([
            len(mock_activity_form['used']),
            len(mock_activity_form['generated']),
            len(mock_activity_form['agents']),
            1
        ])
        new_rels = sum([
            len(mock_activity_form['used']),
            len(mock_activity_form['generated']),
            len(mock_activity_form['agents']) * 2,
        ])

        assert len(mock_graph.nodes) == (node_count + new_nodes)
        assert len(mock_graph.relationships) == (rel_count + new_rels)
        assert builder.activity.id != activity_id