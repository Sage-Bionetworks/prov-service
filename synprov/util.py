import humps
import json
import re
import iso8601
import pytz

from datetime import datetime

from functools import wraps
from hashlib import sha256


def _convert_keys(obj):
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
        return [_convert_keys(i) for i in obj]
    elif isinstance(obj, dict):
        return {(humps.camelize(k.lstrip('_'))
                 if not re.search('^_id', k)
                 else k): _convert_keys(obj[k])
                for k in obj}
    else:
        return obj


def create_hash(values):
    return sha256(bytes(''.join(values), 'utf8')).hexdigest()


def neo4j_to_d3(results):
    nodes = []
    rels = []
    for record in results:
        nodes.append(_convert_node(record['source']))
        nodes.append(_convert_node(record['target']))
        rels.append(_convert_relationship(record['relationship']))
    return {"nodes": nodes, "links": rels}


def get_datetime():
    _date_obj = iso8601.parse_date(datetime.now().isoformat())
    _date_utc = _date_obj.astimezone(pytz.utc)
    return _date_utc.strftime('%Y-%m-%dT%H:%M:%SZ')


def _convert_node(neo4j_node):
    return {
        'id': neo4j_node.identity,
        'labels': list(neo4j_node.labels),
        'properties': dict(neo4j_node)
    }


def _convert_relationship(neo4j_rel):
    return {
        'id': neo4j_rel.identity,
        'type': list(neo4j_rel.types()),
        'startNode': neo4j_rel.start_node.identity,
        'endNode': neo4j_rel.end_node.identity,
        'properties': dict(neo4j_rel),
        'source': neo4j_rel.start_node.identity,
        'target': neo4j_rel.end_node.identity,
        'linknum': 1
    }