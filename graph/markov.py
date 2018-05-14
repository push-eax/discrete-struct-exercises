"""
Kiernan Roche
CSCI 317 
Professor David Keil
Competency 3.2b: Transition system implementation

This is an implementation of an Markov chain algorithm (a type of transition system) in Python, as a class inheriting from AdjList.
This class implements the following methods (not including those inherited from AdjList):
- simulate: Simulates a Markov chain to n steps, from an initial vertex. Returns a list of states.
- weightedChoice: Chooses randomly between linked vertices of a given vertex.
- findPath: This method is overridden so that it doesn't return anything. simulate() is used for path generation.
"""

import random
from adjlist import *

class Markov(AdjList): # Inherit from AdjList
    def __init__(self):
        super().__init__()

    def edgeExists(self, startVertex, endVertex):
        # Return True if both vertices are in each others' lists
        if self.vertexExists(startVertex) and self.vertexExists(endVertex):
            return (startVertex in [x[0] for x in self.graph[endVertex]]) and (endVertex in [x[0] for x in self.graph[startVertex]])

    def addEdge(self, startVertex, endVertex, weight):
        if self.vertexExists(startVertex) and self.vertexExists(endVertex) and (not self.edgeExists(startVertex, endVertex)):
            self.graph[startVertex].append((endVertex, weight))
            self.graph[endVertex].append((startVertex, weight))

    def removeEdge(self, startVertex, endVertex):
        if self.edgeExists(startVertex, endVertex):
            # remove any lists from v that contain startVertex or endVertex
            self.graph[startVertex] = [x for x in self.graph[startVertex] if x[0] != endVertex]
            self.graph[endVertex] = [x for x in self.graph[startVertex] if x[0] != startVertex]

    def removeVertex(self, vertex):
        # Remove the vertex from the graph and the vertex-weight tuple from the lists of all other vertices
        self.graph = {k:[x for x in v if x[0] != vertex] for k,v in self.graph.items() if k != vertex}

    def findPath(self):
        # The Markov class isn't for pathfinding, it's for simulating state changes. We don't need a findPath method
        return None

    def weightedChoice(self, vertex): # Intended as a private method
        weights = [x[1] for x in self.graph[vertex]]
        
        rnd = random.random() * sum(weights)
        
        for i, w in enumerate(weights):
            rnd -= w
            if rnd < 0:
                return self.graph[vertex][i][0]

    def simulate(self, vertex, n): # Simulate n state changes
        path = [vertex]
        
        for i in range(0, n):
            path.append(self.weightedChoice(path[len(path) - 1]))

        return path
           
