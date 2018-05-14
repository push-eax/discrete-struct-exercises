"""
Kiernan Roche
CSCI 317 
Professor David Keil
Competency 0.4c: Graph implementation

This is an implementation of an undirected graph in Python, as a class with the following methods:
- addVertex:    Adds a vertex to the graph, if it does not already exist.
- addEdge:      Adds an edge to the graph, if it does not already exist and its vertices exist.
- removeVertex: Removes a vertex from the graph.
- removeEdge:   Removes an edge from the graph.
- vertexExists: Returns true if the graph contains a vertex, false otherwise.
- edgeExists:   Returns true if an edge exists in the set, false otherwise.
- getVertices:  Return the vertices that exist in the graph.
- getEdges:     Return the edges that exist in the graph.
"""

class Graph:
    def __init__(self):
        self.vertices = []          # Vertices and edges are stored in lists.
        self.edges = []             # Internally, the edges list consists of tuples containing the beginning vertex and the ending vertex, in the form (startVertex, endVertex).

    def vertexExists(self, vertex):
        return vertex in self.vertices

    def edgeExists(self, startVertex, endVertex):
        return ((startVertex, endVertex) in self.edges) or ((endVertex, startVertex) in self.edges) # Check both possible permutations of the edge to ensure that it's removed.

    def addVertex(self, vertex):
        if not self.vertexExists(vertex):   # If the vertex doesn't exist,
            self.vertices.append(vertex)    # add it.

    def addEdge(self, startVertex, endVertex):
        # If both vertices exist and an edge between them does not exist:
        if self.vertexExists(startVertex) and self.vertexExists(endVertex) and (not self.edgeExists(startVertex, endVertex)):
            self.edges.append((startVertex, endVertex)) # add it (as a tuple).

    def removeVertex(self, vertex):
        if not self.vertexExists(vertex):
            return
        
        self.vertices.remove(vertex)
        for item in self.edges:             # Make sure we remove any edges that contain this vertex.
            if vertex in item:              # If an edge exists that contains this vertex,
                self.edges.remove(item)     # remove it.

    def removeEdge(self, startVertex, endVertex):
        for item in self.edges:
            if startVertex in item and endVertex in item:
                self.edges.remove(item)

    def getVertices(self):
        return self.vertices

    def getEdges(self):
        return self.edges
