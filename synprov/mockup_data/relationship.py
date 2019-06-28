import json
import random as r

from synprov.mockup_data.dict import (AgentRoles,
                                      ReferenceRoles,
                                      ActivityClass,
                                      RelationTypes)


class Relationship:

    typesArr = RelationTypes
    agentRoles = AgentRoles
    referenceRoles = ReferenceRoles

    def __init__(self, firstId, secondId, typeId):

        self.agtCount = len(self.agentRoles)
        self.refCount = len(self.referenceRoles)

        self.start_id = firstId
        self.end_id = secondId
        if typeId == 0:
            self.role = self.agentRoles[ r.randrange(self.agtCount) ]
        elif typeId == 3:
            self.role = self.agentRoles[ r.randrange(self.agtCount) ] + ";" + self.referenceRoles[r.randrange(self.refCount)]
        else:
            self.role = self.referenceRoles[r.randrange(self.refCount)]
        self.type = self.typesArr[typeId]

    def getData(self):
        x = {
            ":START_ID": str(self.start_id),
            "roles": self.role,
            ":END_ID": str(self.end_id),
            ":TYPE": self.type
        }

        return json.dumps(x)
