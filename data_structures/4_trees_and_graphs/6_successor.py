from binary_search_tree import in_order_traversal

class Node:
    def __init__(self, parent=None, data=None):
        self.parent = parent
        self.data = data
        self.left = None
        self.right = None

def in_order_successor(tree_node):
    """
        For a given node return in-order successor
    """
    if tree_node == None:
        return None
    
    # if node has right child -> return left most child
    if tree_node.right:
        return left_most_child(tree_node.right)
    else:
        current = tree_node
        ancestor = tree_node.parent
        # Go up until we are on left of parent
        while ancestor and ancestor.left != current:
            current = ancestor
            ancestor = ancestor.parent
        return ancestor

def left_most_child(n):
    """
        Return left most child of node
    """
    if n == None:
        return None
    while n.left:
        n = n.left
    return n


tree = Node(None, 15)
tree.left = Node(tree, 10)
tree.right = Node(tree, 20)
tree.right.left = Node(tree.right, 17)
tree.right.left.left = Node(tree.right.left, 16)
tree.right.right = Node(tree.right, 25)
tree.right.right.right = Node(tree.right.right, 27)
tree.left.left = Node(tree.left, 8)
tree.left.left.left = Node(tree.left.left, 6)
tree.left.right = Node(tree.left, 12)
tree.left.right.left = Node(tree.left.right, 11)
in_order_traversal(tree)
print()
k = in_order_successor(tree.left.right)
print(k.data)
