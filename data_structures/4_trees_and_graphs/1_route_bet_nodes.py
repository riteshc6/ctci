from graph_list import Graph, Node
from collections import deque

def route_bet_nodes(node1, node2):
    """
        Checking if there is a valid path between two nodes of a directed graph.
        BFS Traversal is used
    """
    queue = deque()
    queue.append(node1)
    node1.visited = True

    while len(queue):
        node = queue.popleft()
        if node == node2:
            return True
        for child in node.children:
            if not child.visited:
                queue.append(child)
                child.visited = True
    return False


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

print(route_bet_nodes(node1, node5))