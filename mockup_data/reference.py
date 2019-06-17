import uuid
import json

from dict import refRoles

class Reference:

    roles = refRoles

    def __init__(self, aTargetVer = 1, aRole = 0):
        self.id = uuid.uuid1()
        self.trg_id = aTargetVer
        self.role = self.roles[aRole]

    def setTargetID(self, param):
        self.trg_id = param

    def setRole(self, param):
        self.role = self.roles[param]

    def getRolesCount(self):
        return len(self.roles)

    def getData(self):
        x = {
            "target_id": str(self.id),
            "target_version_id": self.trg_id,
            "role": self.role
        }
        return json.dumps(x)