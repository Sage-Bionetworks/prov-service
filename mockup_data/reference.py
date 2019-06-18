import uuid
import json

class Reference:

    def __init__(self, aTargetId = "", aTargetVer = "1", aName = ""):
        self.id = uuid.uuid1()
        self.trg_id = aTargetId
        self.trg_ver = aTargetVer
        self.name = aName

    def setTargetID(self, param):
        self.trg_id = param

    def setTargetVersion(self, param):
        self.trg_ver = param

    def setName(self, param):
        self.name = param

    def getData(self):
        x = {
            "refId": str(self.id),
            "target_id": self.trg_id,
            "target_version_id": self.trg_ver,
            "name": self.name,
            ":LABEL": "Reference"
        }
        return json.dumps(x)