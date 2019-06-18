import uuid
import json

from dict import ActivityClass

class Activity:

    actArray = ActivityClass

    def __init__(self, aName = "", aClass = 0):
        self.id = uuid.uuid1()
        self.name = aName
        self.class_ = self.actArray[aClass]

    def setName(self, param):
        self.name = param

    def setClass(self, param):
        self.class_ = self.actArray[param]

    def getClassCount(self):
        return len(self.actArray)

    def getData(self):
        x = {
            "actId": str(self.id),
            "name": self.name,
            "class": self.class_,
        }
        return json.dumps(x)
