from typing import List, Tuple
from collections import deque

class Project:
    
    def __init__(self, name):
        self.name = name
        self.children = []
        self.map = {}
        self.dependencies = 0   # Tracks number of incoming edges
    
    def add_neighbour(self, node):
        if not node.name in self.map:
            self.map[node.name] = node
            node.dependencies += 1      # Increment incoming edges count in child
            self.children.append(node)
    

class Graph:

    def __init__(self):
        self.map = {}
        self.nodes = []
    
    def get_or_create_node(self, name: str) -> Project:
        if not self.map.get(name):
            node = Project(name)
            self.map[name] = node
            self.nodes.append(node)
        return self.map.get(name)
    
    def add_edge(self, start_name: str, end_name: str):
        start = self.get_or_create_node(start_name)
        end = self.get_or_create_node(end_name)
        start.add_neighbour(end)


def build_graph(projects: list, dependencies:List[tuple]) -> Graph:
    graph = Graph()
    
    for project in projects:
        graph.get_or_create_node(project)
    
    for dependency in dependencies:
        first = dependency[0]
        second = dependency[1]
        graph.add_edge(first, second)
    
    return graph


def add_non_dependent(order, projects, offset):
    for project in projects:
        if project.dependencies == 0:
            order[offset] = project
            offset += 1
    return offset


def order_projects(projects:List[Project]):

    order = [None] * len(projects)
    end_of_list = add_non_dependent(order, projects, 0)

    to_be_processed = 0
    
    while to_be_processed < len(order):
        current = order[to_be_processed]
        
        if current == None:
            return None

        children = current.children

        # Remove current as incoming edge from children
        for child in children:
            child.dependencies -= 1
        
        end_of_list = add_non_dependent(order, children, end_of_list)
        to_be_processed += 1
    return order


def find_build_order(projects: list, dependencies: list):
    graph = build_graph(projects, dependencies)
    return order_projects(graph.nodes)

    


projects = ["a", "b", "c", "d", "e","f"]
dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c"), ("c", "d")]
order = find_build_order(projects, dependencies)
[print(node.name) for node in order] if order else print("Circular Dependency")


