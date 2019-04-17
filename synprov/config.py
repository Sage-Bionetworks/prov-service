#!/usr/bin/env python3

import os
import connexion

from flask_mongoengine import MongoEngine

from synprov import encoder


connex_app = connexion.App(__name__, specification_dir='./openapi/')

local_uri = 'mongodb://localhost:27017/provDB'
env_uri = os.environ.get('MONGODB_URI')
mongodb_host = env_uri if env_uri is not None else local_uri
connex_app.app.config['MONGODB_SETTINGS'] = {
    'db': 'provDB',
    'host': mongodb_host,
    'port': 27017
}

mongo = MongoEngine(connex_app.app)

# reset encoder
connex_app.app.json_encoder = encoder.MongoEngineJSONEncoder