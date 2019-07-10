#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: June/24/2019
@author: madejp
"""
import logging

from py2neo import Graph, Node

from synprov.mockup_data.dict import NodeRelationships


class GraphDataBase:

   def __init__(self, graphConn):
      self.graph = graphConn

   def create_node(self, prov_object):
      node_data = prov_object.get_data()
      label = node_data.pop('label')
      node = Node(
         label,
         **node_data
      )
      node.__primarylabel__ = label
      node.__primarykey__ = 'id'
      self.graph.merge(node)
      logging.debug("Created node: {}".format(node))

   def create_relationship(self, relationship):
      rel_data = relationship.get_data()
      rel_type = rel_data.pop('type')
      start_end_nodes = [(s, n) for (s, n) in NodeRelationships
                         if NodeRelationships[(s, n)] == rel_type][0]
      start_node = rel_data.pop('start_node')
      end_node = rel_data.pop('end_node')
      rel_props = ', '.join(['{}:"{}"'.format(k, v)
                             for k, v in rel_data.items()])
      query_base = (
         '''
         MATCH (s:{start} {{id:{{start_id}}}}), (e:{end} {{id:{{end_id}}}})
         MERGE (s)-[r:{type} {{{props}}}]->(e)
         RETURN r
         '''
      ).format(
         start = start_end_nodes[0],
         end=start_end_nodes[1],
         type=rel_type,
         props=rel_props
      )
      results = self.graph.run(
         query_base,
         start_id=start_node,
         end_id=end_node
      )
      logging.debug("Created relationship: {}".format(results.data()[0]))

