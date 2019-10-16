import humps
import json
import re
import iso8601
import pytz
import datetime
import six
import typing
import socket

from functools import wraps
from hashlib import sha256


def _deserialize(data, klass):
    """Deserializes dict, list, str into an object.

    :param data: dict, list or str.
    :param klass: class literal, or string of class name.

    :return: object.
    """
    if data is None:
        return None

    if klass in six.integer_types or klass in (float, str, bool):
        return _deserialize_primitive(data, klass)
    elif klass == object:
        return _deserialize_object(data)
    elif klass == datetime.date:
        return deserialize_date(data)
    elif klass == datetime.datetime:
        return deserialize_datetime(data)
    elif type(klass) == typing.GenericMeta:
        if klass.__extra__ == list:
            return _deserialize_list(data, klass.__args__[0])
        if klass.__extra__ == dict:
            return _deserialize_dict(data, klass.__args__[1])
    else:
        return deserialize_model(data, klass)


def _deserialize_primitive(data, klass):
    """Deserializes to primitive type.

    :param data: data to deserialize.
    :param klass: class literal.

    :return: int, long, float, str, bool.
    :rtype: int | long | float | str | bool
    """
    try:
        value = klass(data)
    except UnicodeEncodeError:
        value = six.u(data)
    except TypeError:
        value = data
    return value


def _deserialize_object(value):
    """Return an original value.

    :return: object.
    """
    return value


def deserialize_date(string):
    """Deserializes string to date.

    :param string: str.
    :type string: str
    :return: date.
    :rtype: date
    """
    try:
        from dateutil.parser import parse
        return parse(string).date()
    except ImportError:
        return string


def deserialize_datetime(string):
    """Deserializes string to datetime.

    The string should be in iso8601 datetime format.

    :param string: str.
    :type string: str
    :return: datetime.
    :rtype: datetime
    """
    try:
        from dateutil.parser import parse
        return parse(string)
    except ImportError:
        return string


def deserialize_model(data, klass):
    """Deserializes list or dict to model.

    :param data: dict, list.
    :type data: dict | list
    :param klass: class literal.
    :return: model object.
    """
    instance = klass()

    if not instance.openapi_types:
        return data

    for attr, attr_type in six.iteritems(instance.openapi_types):
        if data is not None \
                and instance.attribute_map[attr] in data \
                and isinstance(data, (list, dict)):
            value = data[instance.attribute_map[attr]]
            setattr(instance, attr, _deserialize(value, attr_type))

    return instance


def _deserialize_list(data, boxed_type):
    """Deserializes a list and its elements.

    :param data: list to deserialize.
    :type data: list
    :param boxed_type: class literal.

    :return: deserialized list.
    :rtype: list
    """
    return [_deserialize(sub_data, boxed_type)
            for sub_data in data]


def _deserialize_dict(data, boxed_type):
    """Deserializes a dict and its elements.

    :param data: dict to deserialize.
    :type data: dict
    :param boxed_type: class literal.

    :return: deserialized dict.
    :rtype: dict
    """
    return {k: _deserialize(v, boxed_type)
            for k, v in six.iteritems(data)}


def convert_keys(obj):
    """
    Convert keys in a dictionary (or nested dictionary) from snake_case
    to camelCase; ignore '_id' keys.

    :param obj: A dict or list of dicts with string keys to be
        converted.
    :type obj: dict, list
    :return: A dict or list of dicts with string keys converted from
        snake_case to camelCase.
    :rtype: dict, list
    """
    if isinstance(obj, list):
        return [convert_keys(i) for i in obj]
    elif isinstance(obj, dict):
        return {(humps.camelize(k.lstrip('_'))
                 if not re.search('^_id', k)
                 else k): convert_keys(obj[k])
                for k in obj}
    else:
        return obj


def quote_string(string):
    try:
        json.loads(string)
    except json.JSONDecodeError:
        string = json.dumps(string)
    return string


def get_datetime(now=None):
    if now is None:
        now = datetime.datetime.now()
    _date_obj = iso8601.parse_date(now.isoformat())
    _date_utc = _date_obj.astimezone(pytz.utc)
    return _date_utc.strftime('%Y-%m-%dT%H:%M:%SZ')


def neo4j_export(results):
    nodes, rels = _convert_results(results)
    return {
        "results": [{
            "columns": ["Activity", "Reference", "Agent"],
            "data": [{
                "graph": {
                    "nodes": nodes,
                    "relationships": rels
                }
            }]
        }]
    }


def neo4j_to_d3(results):
    nodes, rels = _convert_results(results)
    return {"nodes": nodes, "links": rels}


def _convert_results(neo4j_results):
    nodes = []
    node_ids = []
    rels = []
    rel_ids = []
    for record in neo4j_results:
        if record['source'].identity not in node_ids:
            nodes.append(_convert_node(record['source']))
            node_ids.append(record['source'].identity)
        if record['target'].identity not in node_ids:
            nodes.append(_convert_node(record['target']))
            node_ids.append(record['target'].identity)
        if record['relationship'].identity not in rel_ids:
            rels.append(_convert_relationship(record['relationship']))
            rel_ids.append(record['relationship'].identity)
    return nodes, rels


def _convert_node(neo4j_node):
    return {
        'id': str(neo4j_node.identity),
        'labels': list(neo4j_node.labels),
        'properties': dict(neo4j_node)
    }


def _convert_relationship(neo4j_rel):
    return {
        'id': str(neo4j_rel.identity),
        'type': list(neo4j_rel.types()),
        'startNode': str(neo4j_rel.start_node.identity),
        'endNode': str(neo4j_rel.end_node.identity),
        'properties': dict(neo4j_rel),
        'source': str(neo4j_rel.start_node.identity),
        'target': str(neo4j_rel.end_node.identity),
        'linknum': 1
    }


def node_to_dict(neo4j_node):
    return convert_keys(dict(neo4j_node))


def is_open(ip, port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False