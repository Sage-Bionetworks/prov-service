import argparse
from py2neo import Graph, Node

from activity import *
from agent import *
from reference import *
from relationship import *
from graphdatabase import *

# ------------------------------
NUMAGENTS = 5
NUMREFERENCES = 10
NUMACTIVITIES = 30
# ------------------------------

def addActivities(kt):
    x = []
    for i in range(kt):
        tmp = Activity("Activity_" + str(i+1), 0)
        tmp.setClass( r.randrange(tmp.getClassCount()) )
        x.append( tmp )
    return x

def addAgents(kt):
    x = []
    for i in range(kt):
        tmp = Agent("User_" + str(i+1) )
        x.append( tmp )

    return x

def addReference(kt):
    x = []
    for i in range(kt):
        tmp = Reference("TargetID_" + str(i+1), "1.0", "Reference_" + str(i+1) )
        x.append( tmp )

    return x

def addRelationship(firstArr, secondArr, kt):
# Header: ACTIVITY_ID | roles:string[] | AGENT_ID | TYPE
    x = []
    for i in range( len(firstArr) ):
        dl = r.randrange(len(secondArr))
        tmp = Relationship(firstArr[i].id, secondArr[dl].id, kt)
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

gdb = GraphDataBase( Graph(password = "neo4jj") )

# SCRIPT
# step 1 - Create sets of entity references:
print("Generating table of References...")
refArray = addReference(NUMREFERENCES)
for i in refArray:
    gdb.createReferenceNode( i )
    print( i.getData() )
print(" ")

# step 2 - Create agent/user pool:
print("Generating table of Agents...")
agtArray = addAgents(NUMAGENTS)
for i in agtArray:
    gdb.createAgentNode( i )
    print( i.getData() )
print(" ")

# step 3 - Create activities:
print("Generating table of Activities...")
actArray = addActivities(NUMACTIVITIES)
for i in actArray:
    gdb.createActivityNode( i )
    print( i.getData() )
print(" ")

# step 4 - create Activity -> :WASASSOCIATEDWITH -> Agent
print("Generating :ASSOCIATED records")
assArray = addRelationship(actArray, agtArray, 0)
for i in assArray:
    gdb.createRelationshipAssociated( i )
    print( i.getData() )
print(" ")

# step 5 - create Reference -> :WASGENERATEDBY -> Activity
print("Generating :GENERATEDBY records")
assArray = addRelationship(refArray, actArray, 1)
for i in assArray:
    gdb.createRelationshipGenerated( i )
    print( i.getData() )
print(" ")

# step 6 - create Activity-> :USED -> Reference
print("Generating :USED records")
assArray = addRelationship(actArray, refArray, 2)
for i in assArray:
    gdb.createRelationshipUsed( i )
    print( i.getData() )
print(" ")

# step 7 - create Reference -> :ATTRIBUTEDTO -> Agent
print("Generating :ATTRIBUTEDTO records")
assArray = addRelationship(refArray, agtArray, 3)
for i in assArray:
    gdb.createRelationshipAttributed( i )
    print( i.getData() )
print(" ")