"""
    Basic graph implementation using adjacency lists
"""

from collections import deque

class Node:
    def __init__(self,name):
        self.name = name
        self.children = []
        self.visited = False
    
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.name == other.name and self.children == other.children

    def __hash__(self):
        return hash((self.name))
    
    def add_child(self, child):
        if isinstance(child, Node):
            for c in self.children:
                if child == c:
                    raise Exception("Child already exists")
            self.children.append(child)
        else:
            raise Exception("Child doesn't belongs to node instance")
    

    def __str__(self):
        string = f"{self.name} -> "
        for child in self.children:
            string += f"{child.name} "
        return string


class Graph:
    def __init__(self):
        self.nodes = []
        # self.visited 

    def add_node(self, node):
        self.nodes.append(node)

    def  __str__(self):
        return str([str(node) for node in self.nodes])
    
    def dfs(self, root):
        """
            Depth First Search
        """
        print(root.name)
        root.visited = True
        for child in root.children:
            if not child.visited:
                self.dfs(child)
    
    def bfs(self, root):
        """
            Breadth first search using queue
        """
        queue = deque()
        root.visited = True
        queue.append(root)
        while len(queue):
            # Visit nodes in queue
            node = queue.popleft()
            print(node.name)
            # Put children which are not visited inside queue
            for child in node.children:
                if not child.visited:
                    child.visited = True
                    queue.append(child)

    


graph = Graph()
node0 = Node("0")
node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("4")
node5 = Node("5")
node0.add_child(node1)
node0.add_child(node4)
node0.add_child(node5)
node1.add_child(node3)
node1.add_child(node4)
node2.add_child(node1)
node3.add_child(node2)
node3.add_child(node4)
graph.add_node(node0)
graph.add_node(node1)
graph.add_node(node2)
graph.add_node(node3)
graph.add_node(node4)
graph.add_node(node5)
print(graph)
# graph.dfs(node0)
# graph.bfs(node0)