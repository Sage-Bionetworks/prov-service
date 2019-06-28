
from synprov.config import neomod

from synprov.mockup_data.activity import Activity
from synprov.mockup_data.agent import Agent
from synprov.mockup_data.reference import Reference
from synprov.mockup_data.relationship import Relationship
from synprov.mockup_data.graphdatabase import GraphDataBase

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

# --------------------------------------------------------------
# LOADING SCRIPT
# --------------------------------------------------------------
def init_db(numAgents=5, numActivities=30, numReferences=10):

    gdb = GraphDataBase( Graph(neomod.neo.db.url) )

    # step 1 - Create sets of entity references:
    # print("Generating table of References...")
    refArray = addReference(numReferences)
    for i in refArray:
        gdb.createReferenceNode( i )
        # print( i.getData() )

    # step 2 - Create agent/user pool:
    # print("Generating table of Agents...")
    agtArray = addAgents(numAgents)
    for i in agtArray:
        gdb.createAgentNode( i )
        # print( i.getData() )

    # step 3 - Create activities:
    # print("Generating table of Activities...")
    actArray = addActivities(numActivities)
    for i in actArray:
        gdb.createActivityNode( i )
        # print( i.getData() )

    # step 4 - create Activity -> :WASASSOCIATEDWITH -> Agent
    # print("Generating :ASSOCIATED records")
    assArray = addRelationship(actArray, agtArray, 0)
    for i in assArray:
        gdb.createRelationshipAssociated( i )
        # print( i.getData() )

    # step 5 - create Reference -> :WASGENERATEDBY -> Activity
    # print("Generating :GENERATEDBY records")
    assArray = addRelationship(refArray, actArray, 1)
    for i in assArray:
        gdb.createRelationshipGenerated( i )
        # print( i.getData() )

    # step 6 - create Activity-> :USED -> Reference
    # print("Generating :USED records")
    assArray = addRelationship(actArray, refArray, 2)
    for i in assArray:
        gdb.createRelationshipUsed( i )
        # print( i.getData() )

    # step 7 - create Reference -> :ATTRIBUTEDTO -> Agent
    # print("Generating :ATTRIBUTEDTO records")
    assArray = addRelationship(refArray, agtArray, 3)
    for i in assArray:
        gdb.createRelationshipAttributed( i )
        # print( i.getData() )
