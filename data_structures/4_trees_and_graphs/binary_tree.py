"""
    Binary tree can have up to 2 children in each node
"""

class Node:
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def in_order_traversal(tree):
    """
        Traversal order => left -> current -> right
    """
    node = tree
    if node:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)

def pre_order_traversal(tree):
    """
        Traversal order => current -> left -> right
    """
    node = tree
    if node:
        print(node.data, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def post_order_traversal(tree):
    """
        Traversal order => left -> right -> current
    """
    node = tree
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data, end=" ")


if __name__ == "__main__":

    tree = Node(8)
    tree.left = Node(4)
    tree.right = Node(10)
    tree.left.left = Node(2)
    tree.left.right = Node(6)
    tree.right.right = Node(20)
    tree.right.left = Node(14)
    tree.left.right.left = Node(5)

    in_order_traversal(tree)
    print()
    pre_order_traversal(tree)
    print()
    post_order_traversal(tree)
    print()
