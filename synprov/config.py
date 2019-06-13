#!/usr/bin/env python3

import os
import connexion

from flask_neomodel import NeoModel


connex_app = connexion.App(__name__, specification_dir='./openapi/')

env_host = os.environ.get('NEO4J_HOST')
neo4j_host = env_host if env_host is not None else 'localhost'

neomod = NeoModel(connex_app.app, variables={
    'user': 'neo4j',
    'password': '',
    'host': neo4j_host,
    'port': 7687
})
