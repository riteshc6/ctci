"""
    Basic graph implementation using matrix
"""

class Graph:

    def __init__(self, vertex_num):
        self.vertex_num = vertex_num
        self.edges = [[0]* vertex_num for _ in range(vertex_num)]
    
    def add_directed_edge(self, from_vertex, to_vertex):
        if from_vertex < self.vertex_num and to_vertex < self.vertex_num:
            self.edges[from_vertex][to_vertex] = 1
        else:
            raise Exception("Vertex not present in graph")
    
    def print_matrix(self):
        for i in self.edges:
            for j in i:
                print(j, end=" ")
            print("")
    
graph = Graph(4)
graph.add_directed_edge(0, 1)
graph.add_directed_edge(1, 2)
graph.add_directed_edge(2, 0)
graph.add_directed_edge(3,2)

graph.print_matrix()

