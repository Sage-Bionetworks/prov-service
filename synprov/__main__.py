#!/usr/bin/env python3

import connexion

from synprov import create_app
from synprov.config import neo4j_connection as graph
from synprov.graph.client import GraphClient
from synprov.mock.main import create_mock_graph


def init_db(num_activities=30):
    graph.run(
        '''
        MATCH (n)
        DETACH DELETE n
        '''
    )
    create_mock_graph(GraphClient(graph), num_activities)


def main():
    app = create_app()

    init_db()
    app.run(host='localhost', port=8080)


if __name__ == '__main__':
    main()
