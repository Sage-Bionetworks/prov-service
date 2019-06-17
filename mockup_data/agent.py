import uuid
import json
from dict import agtRoles

class Agent:

    roles = agtRoles

    def __init__(self, aRole = 0):
        self.id = uuid.uuid1()
        self.role = self.roles[aRole]

    def setRole(self, param):
        self.role = self.roles[param]

    def getRolesCount(self):
        return len(self.roles)

    def getData(self):
        x = {
            "agent_id": str(self.id),
            "role": self.role
        }
        return json.dumps(x)