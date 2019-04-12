
from mongoengine.errors import NotUniqueError

from synprov.config import mongo
from synprov.models.mongoengine import Activity, Agent, Reference


def init_db():

    try:
        ref1 = Reference(target_id='entity1',
                        target_version_number=1)
        ref1.save() 

        ref2 = Reference(target_id='entity2',
                        target_version_number=1)
        ref2.save()

        ref3 = Reference(target_id='entity3',
                        target_version_number=1)
        ref3.save()

        agent1 = Agent(agent_id='agent1')
        agent1.save()

        agent2 = Agent(agent_id='agent2')
        agent2.save()

        activity1 = Activity(activity_id='activity1',
                            name='entity1->entity2',
                            description='agent1 generates entity2 from entity1',
                            used=[ref1],
                            generated=[ref2],
                            agents=[agent1])
        activity1.save() 

        activity2 = Activity(activity_id='activity2',
                            name='entity2->entity3',
                            description='agent2 generates entity3 from entity2',
                            used=[ref2],
                            generated=[ref3],
                            agents=[agent2])  
        activity2.save()  
    except NotUniqueError:
        pass

