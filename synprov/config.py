#!/usr/bin/env python3

import connexion

from flask_mongoengine import MongoEngine
from synprov import encoder


connex_app = connexion.App(__name__, specification_dir='./openapi/')

app = connex_app.app
app.config['MONGODB_SETTINGS'] = {
    'db': 'provDB',
    'host': 'mongodb://localhost:27017/provDB',
    'port': 27017
}
app.json_encoder = encoder.JSONEncoder

mongo = MongoEngine(app)