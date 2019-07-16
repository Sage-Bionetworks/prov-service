#!/usr/bin/env python3
import logging
import os
import connexion

from py2neo import Graph

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


connex_app = connexion.App(__name__, specification_dir='./openapi/')

env_host = os.environ.get('NEO4J_HOST')
neo4j_host = env_host if env_host is not None else '0.0.0.0'
env_scheme = os.environ.get('NEO4J_SCHEME')
neo4j_scheme = env_scheme if env_scheme is not None else 'bolt'

neo_user = os.environ['NEO4J_USERNAME']
neo_pass = os.environ['NEO4J_PASSWORD']

logger.info("Connecting to neo4j database")
neo4j_connection = Graph(
    scheme=neo4j_scheme,
    host=neo4j_host,
    user=neo_user,
    password=neo_pass
)
