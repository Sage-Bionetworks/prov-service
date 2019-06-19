import uuid
import json

class Agent:

    def __init__(self, aName = ""):
        self.id = uuid.uuid1()
        self.name = aName

    def setName(self, param):
        self.name = param

    def getData(self):
        x = {
            "agtId": str(self.id),
            "name": self.name,
            ":LABEL": "Agent"
        }
        return json.dumps(x)