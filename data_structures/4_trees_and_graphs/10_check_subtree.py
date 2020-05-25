from binary_tree import Node
from collections import deque

def check_subtree(T1, T2):
    if isinstance(T1, Node) and isinstance(T2, Node):
        subtree = find_subtree(T1, T2)

        if subtree:
            return is_equal(subtree, T2)
        else:
            return False
    else:
        raise Exception("Please give Arguments of class Node")

def find_subtree(tree, subtree):
    queue = deque()
    queue.append(tree)
    while len(queue):
        node = queue.popleft()
        if node.data == subtree.data:
            return node
        
        if node.left:
            queue.append(node.left)
        
        if node.right:
            queue.append(node.right)
    return None


def is_equal(subtree, T2):
    queue1 = deque()
    queue1.append(subtree)
    queue2 = deque()
    queue2.append(T2)

    while len(queue1) or len(queue2):
        if len(queue1) == len(queue2):
            node1 = queue1.popleft()
            node2 = queue2.popleft()

            if node1.data == node2.data:
                if  node1.left and node2.left:
                    queue1.append(node1.left)
                    queue2.append(node2.left)
                elif node1.left or node2.left:
                    return False

                if node1.right and node2.right:
                    queue1.append(node1.right)
                    queue2.append(node2.right)
                elif node1.right or node2.right:
                    return False
            else:
                return False
        else:
            return False

    return True


tree = Node(12, Node(6), Node(20))
tree.left.left = Node(3, Node(1), Node(4))
tree.left.right = Node(8, Node(7), Node(10))
tree.left.right.right.right = Node(11)
tree.left.right.right.left = Node(9)
tree.right.left = Node(14)
tree.right.right = Node(24)
T2 = Node(8, Node(7), Node(10))
T2.right.right = Node(11)
T2.right.left = Node(9)
T3 = Node(20,Node(14), Node(28))

print(check_subtree(tree, T2))
print(check_subtree(tree, T3))
