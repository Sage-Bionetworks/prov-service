import connexion
import six
import uuid

from synprov.models.activity import Activity  # noqa: E501
from synprov.models.activity_request import ActivityRequest  # noqa: E501
from synprov import util
from synprov.config import mongo


def create_activity(body):  # noqa: E501
    """Create a new.

    Create a new Activity. If the passed Activity object contains a Used array, you must set the concreteType field of each Used subclass. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Activity
    """
    # if connexion.request.is_json:
    #     body = JsonActivityRequest.from_dict(connexion.request.get_json())  # noqa: E501
    activity = Activity(**body)
    activity.id = uuid.uuid4().hex
    activity_id = mongo.db.activities.insert_one(activity.to_dict()).inserted_id
    return Activity.from_dict(mongo.db.activities.find_one({'_id': activity_id}))


def delete_activity(id):  # noqa: E501
    """Delete an.

    Delete an Activity # noqa: E501

    :param id: The id of activity to delete.
    :type id: str

    :rtype: file
    """
    return 'do some magic!'


def get_activity(id):  # noqa: E501
    """Get an existing.

    Get an existing Activity # noqa: E501

    :param id: The ID of the activity to fetch.
    :type id: str

    :rtype: Activity
    """
    return Activity.from_dict(mongo.db.activities.find_one({'id': id}))


def list_activities():  # noqa: E501
    """.

    List Activities # noqa: E501


    :rtype: List[Activity]
    """
    return 'do some magic!'


def update_activity(id, body=None):  # noqa: E501
    """Update an.

    Update an Activity # noqa: E501

    :param id: The id of the activity to update.
    :type id: str
    :param body: Update an Activity
    :type body: dict | bytes

    :rtype: Activity
    """
    if connexion.request.is_json:
        body = ActivityRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
