#!/usr/bin/env python3

import connexion

from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
from synprov import encoder


connex_app = connexion.App(__name__, specification_dir='./openapi/')

app = connex_app.app
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/prov_db'
app.config['MONGODB_SETTINGS'] = {
    'db': 'prov_db',
    'host': 'mongodb://localhost:27017/prov_db',
    'port': 27017
}
app.json_encoder = encoder.JSONEncoder

mongo = MongoEngine(app)