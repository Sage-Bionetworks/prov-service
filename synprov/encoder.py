from bson import json_util
import six
import json

from connexion.apps.flask_app import FlaskJSONEncoder	
from mongoengine.base import BaseDocument, BaseList
from mongoengine.queryset import QuerySet

from synprov.util import _convert_keys	


class MongoEngineJSONEncoder(FlaskJSONEncoder):
    """
    A JSONEncoder which provides serialization of MongoEngine
    documents and queryset objects.
    """
    def default(self, obj):
        if isinstance(obj, BaseDocument):
            data = _convert_keys(obj.to_mongo())
            return json_util._json_convert(data)
        elif isinstance(obj, BaseList):
            data = [_convert_keys(d.to_mongo()) for d in obj]
            return json_util._json_convert(data)
        elif isinstance(obj, QuerySet):
            return json_util._json_convert(obj.as_pymongo())
        return FlaskJSONEncoder.default(self, obj)