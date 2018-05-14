"""
Kiernan Roche
CSCI 317 
Professor David Keil
Competency 3.1b: Graph algorithm implementation

This is an implementation of an adjacency list and pathfinding algorithm in Python, as a class with the following methods:
- addVertex:    Adds a vertex to the graph, if it does not already exist.
- addEdge:      Adds an edge to the graph, if it does not already exist and its vertices exist.
- removeVertex: Removes a vertex from the graph.
- removeEdge:   Removes an edge from the graph.
- vertexExists: Returns true if the graph contains a vertex, false otherwise.
- edgeExists:   Returns true if an edge exists in the set, false otherwise.
- getGraph:     Return the internal representation of the graph.
- findPath:     Returns the shortest path between two vertices, or None if no such path exists. Recursive.
"""

class AdjList:
    def __init__(self):
        self.graph = {}

    def vertexExists(self, vertex):
        return vertex in self.graph.keys()

    def edgeExists(self, startVertex, endVertex):
        # Return True if both vertices are in each others' lists
        if self.vertexExists(startVertex) and self.vertexExists(endVertex):
            return (startVertex in self.graph[endVertex]) and (endVertex in self.graph[startVertex])
        return False

    def addVertex(self, vertex):
        self.graph[vertex] = []
    
    def removeVertex(self, vertex):
        # Remove the vertex from the graph and the lists of all other vertices
        self.graph = {k:[x for x in v if x != vertex] for k,v in self.graph.items() if k != vertex}
    
    def addEdge(self, startVertex, endVertex):
        # If both vertices exist and the edge doesn't already exist:
        if self.vertexExists(startVertex) and self.vertexExists(endVertex) and (not self.edgeExists(startVertex, endVertex)):
            # Append both vertices to each others' lists
            self.graph[startVertex].append(endVertex)
            self.graph[endVertex].append(startVertex)

    def removeEdge(self, startVertex, endVertex):
        # If the edge exists:
        if self.edgeExists(startVertex, endVertex):
            # Remove both vertices from each others' lists
            self.graph[startVertex].remove(endVertex)
            self.graph[endVertex].remove(startVertex)
        
    def getGraph(self):
        return self.graph
    
    def findPath(self, startVertex, endVertex, path=[]):
        path = path + [startVertex]
        if startVertex == endVertex:
            return path
        if not self.vertexExists(startVertex):
            return None
        shortest = None
        for node in self.graph[startVertex]:
            if node not in path:
                newpath = self.findPath(node, endVertex, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

