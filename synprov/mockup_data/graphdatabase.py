#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: June/24/2019
@author: madejp
"""

from py2neo import Graph, Node

class GraphDataBase:

   def __init__(self, graphConn):
      self.graph = graphConn

   def createActivityNode(self, myArr):
      # create activity node
      nodeAct = Node("Activity", id=str(myArr.id), name=myArr.name, class_=myArr.class_)
      self.graph.create(nodeAct)

   def createAgentNode(self, myArr):
      # create agent node
      nodeAgt = Node("Agent", id=str(myArr.id), name=myArr.name)
      self.graph.create(nodeAgt)

   def createReferenceNode(self, myArr):
      # create reference node
      nodeRef = Node("Reference", id=str(myArr.id), target_id=myArr.trg_id, target_version_id=myArr.trg_ver, name=myArr.name)
      self.graph.create(nodeRef)

   def createRelationshipUsed(self, myArr):
      self.graph.run(
         'MATCH (a:Activity {id: {startId}}), (r:Reference {id: {endId}}) \
         CREATE (a)-[:USED { roles: {roles} }]->(r)',
         startId=str(myArr.start_id), endId=str(myArr.end_id), roles=myArr.role)

   def createRelationshipAssociated(self, myArr):
      self.graph.run(
         'MATCH (a:Activity {id: {startId}}), (r:Agent {id: {endId}}) \
         CREATE (a)-[:WASASSOCIATEDWITH { roles: {roles}  }]->(r)',
         startId=str(myArr.start_id), endId=str(myArr.end_id), roles=myArr.role)

   def createRelationshipGenerated(self, myArr):
      self.graph.run(
         'MATCH (a:Reference {id: {startId}}), (r:Activity {id: {endId}}) \
         CREATE (a)-[:WASGENERATEDBY { roles: {roles} }]->(r)',
         startId=str(myArr.start_id), endId=str(myArr.end_id), roles=myArr.role)

   def createRelationshipAttributed(self, myArr):
      self.graph.run(
         'MATCH (a:Reference {id: {startId}}), (r:Agent {id: {endId}}) \
         CREATE (a)-[:WASATTRIBUTEDTO { roles: {roles} }]->(r)',
         startId=str(myArr.start_id), endId=str(myArr.end_id), roles=myArr.role)