#!/usr/bin/env python3

import os
import connexion

from py2neo import Graph


connex_app = connexion.App(__name__, specification_dir='./openapi/')

env_host = os.environ.get('NEO4J_HOST')
neo4j_host = env_host if env_host is not None else 'localhost'
print(neo4j_host)

neo_user = os.environ['NEO4J_USERNAME']
neo_pass = os.environ['NEO4J_PASSWORD']

neo4j_connection = Graph(
    scheme='bolt',
    host=neo4j_host,
    user=neo_user,
    password=neo_pass
)
