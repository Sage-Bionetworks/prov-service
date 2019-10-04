import logging
import pytest

from synprov.graph.models.activity import GraphActivity
from synprov.graph.editor import ActivityEditor


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestActivityEditor:

    def test_init(self, mock_graph, mock_activity_id):
        editor = ActivityEditor(
            mock_activity_id
        )
        assert type(editor.activity) is GraphActivity
