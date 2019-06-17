import uuid
import json

class Reference:

    roles = ["data", "tool", "state", "message", "report"]

    def __init__(self, aTargetVer, aRole):
        self.id = uuid.uuid1()
        self.trg_id = aTargetVer
        if type(aRole) is int:
            self.role = self.roles[aRole]
        else:
            self.role = aRole

    def setTargetID(self, param):
        self.trg_id = param

    def setRole(self, param):
        if type(param) is int:
            self.role = self.roles[param]
        else:
            self.role = param

    def getRolesCount(self):
        return len(self.roles)

    def getData(self):
        x = {
            "target_id": str(self.id),
            "target_version_id": self.trg_id,
            "role": self.role
        }
        return json.dumps(x)