"""
Kiernan Roche
CSCI 317 
Professor David Keil

This is a test script for the Graph and AdjList classes, for competencies 3.1b and 0.4c.

"""

from graph import *
from adjlist import *
from markov import *

def main():
    print("Testing all methods of Graph class")

    graph = Graph()             # Instantiate the AdjList class.

    for i in range(0,5):
        graph.addVertex(i + 1)  # add 5 vertices to the graph

    print(graph.getVertices())  # [1, 2, 3, 4, 5]
    print(graph.getEdges())     # {1: [], 2: [], 3: [], 4: [], 5: []}

    graph.addEdge(1, 2)         # add edge from vertex 1 to vertex 2
    graph.addEdge(2, 3)         # add edge from vertex 2 to vertex 3
    graph.addEdge(4, 1)         # add edge from vertex 4 to vertex 1
    print(graph.getEdges())     # [(1, 2), (2, 3), (4, 1)]
    
    graph.addEdge(3, 2)         # This edge was added already
    print(graph.getEdges())     # [(1, 2), (2, 3), (4, 1)]

    graph.addEdge(12, 3)        # Try to add an edge with a nonexistent vertex
    print(graph.getEdges())     # [(1, 2), (2, 3), (4, 1)]

    graph.removeVertex(5)       # Remove a vertex with no edges
    print(graph.getVertices())  # [1, 2, 3, 4]

    graph.removeVertex(4)       # Remove a vertex with edges
    print(graph.getVertices())  # [1, 2, 3]
    print(graph.getEdges())     # [(1, 2), (2, 3)]
    
    graph.removeEdge(2, 3)      # Remove an edge
    print(graph.getEdges())     # [(1, 2)]

    graph.removeEdge(4, 3)      # Remove a nonexistent edge
    print(graph.getEdges())     # [(1, 2)]

    print(graph.vertexExists(1))# Check whether a vertex exists (True)
    print(graph.vertexExists(5))# Check whether a nonexistent vertex exists (False)

    print(graph.edgeExists(1,2))# Check whether an edge exists (True)
    print(graph.edgeExists(2,1))# Test commutability of edgeExists() (True)
    print(graph.edgeExists(3,4))# Check whether a nonexistent edge exists (False)

    print("\n\n")

    print ("Testing all methods of AdjList class")
    
    adjlist = AdjList()           # Instantiate the AdjList class.
    
    for i in range(0,5):
        adjlist.addVertex(i + 1)  # add 5 vertices to the graph

    print(adjlist.getGraph())     # {1: [], 2: [], 3: [], 4: [], 5: []}

    adjlist.addEdge(1, 2)         # add edge from vertex 1 to vertex 2
    adjlist.addEdge(2, 3)         # add edge from vertex 2 to vertex 3
    adjlist.addEdge(4, 1)         # add edge from vertex 4 to vertex 1
    print(adjlist.getGraph())     # {1: [2, 4], 2: [1, 3], 3: [2], 4: [1], 5: []}
    
    adjlist.addEdge(3, 2)         # This edge was added already
    print(adjlist.getGraph())     # {1: [2, 4], 2: [1, 3], 3: [2], 4: [1], 5: []}

    adjlist.addEdge(12, 3)        # Try to add an edge with a nonexistent vertex
    print(adjlist.getGraph())     # {1: [2, 4], 2: [1, 3], 3: [2], 4: [1], 5: []}

    adjlist.removeVertex(5)       # Remove a vertex with no edges
    print(adjlist.getGraph())     # {1: [2, 4], 2: [1, 3], 3: [2], 4: [1]}
    
    adjlist.removeVertex(4)       # Remove a vertex with edges
    print(adjlist.getGraph())     # {1: [2], 2: [1, 3], 3: [2]}
    
#    adjlist.removeEdge(2, 3)      # Remove an edge
#    print(adjlist.getGraph())     # {1: [2], 2: [1], 3: []}

    adjlist.removeEdge(4, 3)      # Remove a nonexistent edge
    print(adjlist.getGraph())     # {1: [2], 2: [1], 3: []}

    print(adjlist.vertexExists(1))# Check whether a vertex exists (True)
    print(adjlist.vertexExists(5))# Check whether a nonexistent vertex exists (False)

    print(adjlist.edgeExists(1,2))# Check whether an edge exists (True)
    print(adjlist.edgeExists(2,1))# Test commutability of edgeExists() (True)
    print(adjlist.edgeExists(3,4))# Check whether a nonexistent edge exists (False)

    print(adjlist.findPath(1, 3)) # Find a path from 1 to 3

    print("\n\n")    

    print("Testing Markov class")
    
    markov = Markov()                   # Markov inherits from AdjList so not all methods will be tested.
    
    for i in range(0,5):
        markov.addVertex(i + 1)         # Add 5 vertices to the graph
    
    print(markov.getGraph())            # {1: [], 2: [], 3: [], 4: [], 5: []}
    
    markov.addEdge(1, 2, 0.5)           # Add edge from vertex 1 to vertex 2 with weight 0.5
    markov.addEdge(1, 3, 0.4)           # Add edge from vertex 1 to vertex 3 with weight 0.4
    markov.addEdge(4, 2, 0.2)           # Add edge from vertex 4 to vertex 2 with weight 0.2
    markov.addEdge(3, 5, 0.35)          # Add edge from vertex 3 to vertex 5 with weight 0.35
    markov.addEdge(5, 1, 0.23)          # Add edge from vertex 5 to vertex 1 with weight 0.23
    markov.addEdge(4, 1, 0.1)           # Add edge from vertex 4 to vertex 1 with weight 0.1
    
    print(markov.getGraph())            # {1: [(2, 0.5), (3, 0.4), (5, 0.23), (4, 0.1)], ..., 5: [(3, 0.35), (1, 0.23)]}

    print(markov.simulate(1, 10))       # Simulate 10 state changes from initial vertex 1
    print(markov.simulate(3, 100))      # Simulate 100 state changes from initial vertex 3
    

if __name__ == "__main__":
    main()
