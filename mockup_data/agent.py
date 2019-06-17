import uuid
import json

class Agent:

    roles = ["Role_1", "Role_2", "Role_3", "Role_4", "Role_5"]

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