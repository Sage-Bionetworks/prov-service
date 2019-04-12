import connexion
import six
import uuid

from mongoengine.errors import NotUniqueError

from synprov.models import Activity  # noqa: E501
from synprov.models import Agent  # noqa: E501
from synprov.models import Reference  # noqa: E501
from synprov.util import convert_keys
from synprov.config import mongo


@convert_keys
def create_activity(body):  # noqa: E501
    """Create a new.

    Create a new Activity. If the passed Activity object contains a Used array, you must set the concreteType field of each Used subclass. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Activity
    """
    for u in body['used']:
        try:
            Reference(**u).save()
        except NotUniqueError:
            continue

    for generated in body['generated']:
        try:
            Reference(**generated).save()
        except NotUniqueError:
            continue

    for a in body['agents']:
        try:
            Agent(**a).save()
        except NotUniqueError:
            continue
    
    activity = Activity(**body)
    activity.activity_id = uuid.uuid4().hex
    activity.save()

    return activity.to_json()


def delete_activity(id):  # noqa: E501
    """Delete an.

    Delete an Activity # noqa: E501

    :param id: The id of activity to delete.
    :type id: str

    :rtype: file
    """
    return 'do some magic!'


@convert_keys
def get_activity(id):  # noqa: E501
    """Get an existing.

    Get an existing Activity # noqa: E501

    :param id: The ID of the activity to fetch.
    :type id: str

    :rtype: Activity
    """
    return Activity.objects(activity_id=id).to_json()


@convert_keys
def list_activities():  # noqa: E501
    """.

    List Activities # noqa: E501


    :rtype: List[Activity]
    """
    return Activity.objects().to_json()


@convert_keys
def update_activity(id, body=None):  # noqa: E501
    """Update an.

    Update an Activity # noqa: E501

    :param id: The id of the activity to update.
    :type id: str
    :param body: Update an Activity
    :type body: dict | bytes

    :rtype: Activity
    """
    return 'do some magic!'
