import sys
import logging
import argparse

from random import randrange
from py2neo import Graph, Node

from synprov.mockup_data.activity import MockActivity
from synprov.mockup_data.mocker import ActivityMocker
from synprov.mockup_data.graphdatabase import GraphDataBase


logging.basicConfig(format='%(asctime)s | %(levelname)s : %(message)s',
                    level=logging.INFO,
                    stream=sys.stdout)

# ------------------------------
NUMACTIVITIES = 30
# ------------------------------


def add_activities(kt):
    x = []
    for i in range(kt):
        tmp = MockActivity(name='Activity_' + str(i+1),
                           class_idx=0)
        tmp.select_class(randrange(tmp.get_class_count()))
        x.append(tmp)
    return x


def create_mock_graph(graph_db, NUMACTIVITIES):
    # SCRIPT

    # step 1 - Create activities:
    logging.info("Generating table of Activities...")
    activity_array = add_activities(NUMACTIVITIES)

    # step 2 - Create corresponding nodes and relationships
    # for each activity:
    ref_num = 0
    agt_num = 0
    for i in activity_array:
        logging.info("Building Activity '{}' of class '{}'"
                     .format(i.name, i._class))
        act = ActivityMocker(graph_db, i, ref_num, agt_num)
        (rn, an) = act.save()
        ref_num += rn
        agt_num += an


# read input parameters
parser = argparse.ArgumentParser(
    description='Generate sample provenance records.'
)
parser.add_argument('nActivities',
                    metavar='#Activities',
                    type=int,
                    nargs='+',
                    default=30,
                    help='number of Activities')


def main():
    args = parser.parse_args()

    # update reference values if needed
    NUMACTIVITIES = args.nActivities[0]

    gdb = GraphDataBase(Graph(password = "neo4jj"))
    create_mock_graph(gdb, NUMACTIVITIES)


if __name__ == "__main__":
    main()