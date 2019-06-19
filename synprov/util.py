import humps
import json
import re

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

