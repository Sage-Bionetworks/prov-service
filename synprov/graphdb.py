from synprov.graphmodels import Activity, Agent, Reference


def init_db():
    act = Activity(
        description='',
        name='entity1->entity2',
        used=[{'target_id': 'entity1', 'target_version_id': '1'}],
        generated=[{'target_id': 'entity2', 'target_version_id': '1'}],
        agents=[{'agent_id': 'agent1'}]
    )
    act.save()

    act = Activity(
        description='',
        name='entity2+entity3->entity4',
        used=[{'target_id': 'entity2', 'target_version_id': '1'},
              {'target_id': 'entity3', 'target_version_id': '1'}],
        generated=[{'target_id': 'entity4', 'target_version_id': '1'}],
        agents=[{'agent_id': 'agent2'}]
    )
    act.save()

    act = Activity(
        description='',
        name='entity2->entity5',
        used=[{'target_id': 'entity2', 'target_version_id': '1'}],
        generated=[{'target_id': 'entity5', 'target_version_id': '1'}],
        agents=[{'agent_id': 'agent3'}]
    )
    act.save()
