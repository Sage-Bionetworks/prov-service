from py2neo import Graph

from synprov.config import neomod
from synprov.mockup_data.main import create_mock_graph
from synprov.mockup_data.graphdatabase import GraphDataBase

graph = Graph(neomod.neo.db.url)

# --------------------------------------------------------------
# LOADING SCRIPT
# --------------------------------------------------------------
def init_db(num_activities=30):
    graph.run(
        '''
        MATCH (n)
        DETACH DELETE n
        '''
    )
    create_mock_graph(GraphDataBase(graph), num_activities)
