#!/usr/bin/env python3

import os
import connexion

from flask_mongoengine import MongoEngine


connex_app = connexion.App(__name__, specification_dir='./openapi/')

app = connex_app.app
local_uri = 'mongodb://localhost:27017/provDB'
env_uri = os.environ.get('MONGODB_URI')
mongodb_host = env_uri if env_uri is not None else local_uri
app.config['MONGODB_SETTINGS'] = {
    'db': 'provDB',
    'host': mongodb_host,
    'port': 27017
}

mongo = MongoEngine(app)