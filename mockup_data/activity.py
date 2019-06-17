import uuid
import json

class Activity:

    actArray = ["Tool session", "Mention", "Report generation"]

    def __init__(self, aName = 0, aDesc="", aUsed=[], aGene=[], aAgent=[]):
        self.id = uuid.uuid1()
        self.name = self.actArray[aName]
        self.description = aDesc
        self.used = aUsed
        self.generated = aGene
        self.agents = aAgent

    def setName(self, param):
        self.name = self.actArray[param]

    def setDescription(self, param):
        self.description = param

    def addUsed(self, param):
        self.used.append(param)

    def addGenerated(self, param):
        self.generated.append(param)

    def addAgent(self, param):
        self.agents.append(param)

    def getNameCount(self):
        return len(self.actArray)

    def getData(self):
        x = {
            "activity_id": str(self.id),
            "name": self.name,
            "description": self.description,
            "used": self.used,
            "generated": self.generated,
            "agents": self.agents
        }
        return json.dumps(x)
