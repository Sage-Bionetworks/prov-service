
from graphene import ObjectType, Schema
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from synprov.models import Activity as ActivityModel
from synprov.models import Agent as AgentModel
from synprov.models import Reference as ReferenceModel


class Reference(MongoengineObjectType):
    class Meta:
        model = ReferenceModel
        interfaces = (Node, )


class Agent(MongoengineObjectType):
    class Meta:
        model = AgentModel
        interfaces = (Node, )


class Activity(MongoengineObjectType):
    class Meta:
        model = ActivityModel
        interfaces = (Node, )


class Query(ObjectType):
    node = Node.Field()
    all_activities = MongoengineConnectionField(Activity)
    all_agents = MongoengineConnectionField(Agent)
    all_references = MongoengineConnectionField(Reference)


schema = Schema(query=Query, types=[Activity, Agent, Reference])