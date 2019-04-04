#!/usr/bin/env python3

import connexion

from flask_pymongo import PyMongo
from synprov import encoder


connex_app = connexion.App(__name__, specification_dir='./openapi/')

app = connex_app.app
app.config['MONGO_URI'] = 'mongodb://localhost:27017/prov_db'
app.json_encoder = encoder.JSONEncoder

mongo = PyMongo(app)