from binary_search_tree import in_order_traversal, Node as bst

class Node(bst):
    def __init__(self, data=None):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

def in_order_successor(tree_node):
    if tree_node == None:
        return None
    
    if tree_node.right:
        return left_most_child(tree_node.right)
    else:
        q = tree_node
        x = tree_node.parent
    
        while x and x.left == q:
            q = x
            x = x.parent
        return x

def left_most_child(n):
    if n == None:
        return None
    while n.left:
        n = n.left
    return n


tree = Node(8)
tree.left = Node(4)
tree.right = Node(12)
tree.left.parent = tree
tree.right.parent = tree
tree.right.left = Node(10)
tree.right.left.parent = tree.right
print(in_order_successor(tree).data)
