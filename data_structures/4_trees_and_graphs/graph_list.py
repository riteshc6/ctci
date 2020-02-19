"""
    Basic gragh implementation using adjacency lists
"""

class Graph:
    def __init__(self, num_vertex):
        self.vertexes = {i:[] for i in range(num_vertex)}

    def add_edge(self, from_vertex, to_vertex):
        self.vertexes[from_vertex].append(to_vertex)

    def __str__(self):
        return str(self.vertexes)



graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(3,2)
graph.add_edge(3, 0)
print(graph)
