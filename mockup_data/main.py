import random as r
import argparse

from activity import *
from agent import *
from reference import *

# ------------------------------
NUMAGENTS = 5
NUMREFERENCES = 10
NUMACTIVITIES = 30
# ------------------------------

def getDataID(param, what):
    for i in param:
        if i.role == what:
            return str(i.id)

def addActivities(kt, agents, references):
    x = []
    for i in range(kt):
        tmp = Activity(0, "", [], [], [] )
        tmp.setName( r.randrange(tmp.getNameCount()) )
        tmp.setDescription( "This is description for: " + tmp.name)
        if tmp.name == "Tool session":
            tmp.addUsed( getDataID(references, "data") )
            tmp.addUsed( getDataID(references, "tool") )
            tmp.addGenerated( getDataID(references, "state") )
        elif tmp.name == "Mention":
            tmp.addUsed( getDataID(references, "data") )
            tmp.addUsed( getDataID(references, "tool") )
            tmp.addUsed( getDataID(references, "state") )
            # tmp.addUsed(references, "message")
            tmp.addUsed( getDataID(references, "report") )
            tmp.addGenerated( getDataID(references, "message") )
        else:
            tmp.addUsed( getDataID(references, "state") )
            tmp.addUsed( getDataID(references, "message") )
            tmp.addGenerated( getDataID(references, "report") )
        tmp.addAgent( str(agents[r.randrange(NUMAGENTS)].id) )
        x.append( tmp )
    return x

def addAgents(kt):
    x = []
    for i in range(kt):
        tmp = Agent(0)
        tmp.setRole( r.randrange(tmp.getRolesCount()) )
        x.append( tmp )

    return x

def addReference(kt):
    x = []
    for i in range(kt):
        tmp = Reference(1, 0)
        tmp.setRole( r.randrange(tmp.getRolesCount()) )
        x.append( tmp )

    return x

# read input parameters
parser = argparse.ArgumentParser(description='Generate sample provenance records.')
parser.add_argument('nAgents', metavar='#Agents', type=int, nargs='+', default=5, help='number of Agents')
parser.add_argument('nReferences', metavar='#References', type=int, nargs='+', default=10, help='number of References')
parser.add_argument('nActivities', metavar='#Activities', type=int, nargs='+', default=30, help='number of Activities')
args = parser.parse_args()

# update reference values if needed
NUMACTIVITIES = args.nActivities[0]
NUMAGENTS = args.nAgents[0]
NUMREFERENCES = args.nReferences[0]

# SCRIPT
# step 1 - Create sets of entity references:
print("Generating table of References...")
refArray = addReference(NUMREFERENCES)
for i in refArray:
    print( i.getData() )
print(".")

# step 2 - Create agent/user pool:
print("Generating table of Agents...")
agtArray = addAgents(NUMAGENTS)
for i in agtArray:
    print( i.getData() )
print(".")

# step 3 - Create activities:
print("Generating table of Activities...")
actArray = addActivities(NUMACTIVITIES, agtArray, refArray)
for i in actArray:
    print( i.getData() )
print(".")