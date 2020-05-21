from binary_tree import Node as binary_tree_node, in_order_traversal

class Node(binary_tree_node):
    def __init__(self, data, left=None, right=None):
        super().__init__(data, left, right)
        self.parent = None


def first_common_ancestor(node1: Node, node2: Node) -> Node:
    """
    Returns the first common ancestor
    """
    ancestors_1 = set(); ancestors_2 = set()  # Keep track of ancestors of both nodes
    # Initialize parents and add to ancestors
    parent1 = node1
    ancestors_1.add(parent1)
    parent2 = node2
    ancestors_2.add(parent2)

    while parent1 and parent2:

        if parent1:
            if parent1.data in ancestors_2:
                return parent1
            parent1 = parent1.parent
            ancestors_1.add(parent1.data)
        
        if parent2:
            if parent2.data in ancestors_1:
                return parent2
            parent2 = parent2.parent
            ancestors_2.add(parent2.data)
    return None

tree = Node(5, Node(8), Node(10))
tree.left.parent = tree
tree.right.parent = tree
tree.left.left = Node(11, Node(20), Node(21))
tree.left.left.parent = tree.left
tree.left.left.left.parent = tree.left.left
tree.left.left.right.parent = tree.left.left
tree.left.right = Node(12, Node(22, Node(24), Node(25)), Node(23))
tree.left.right.parent = tree.left
tree.left.right.left.parent = tree.left.right
tree.left.right.right.parent = tree.left.right
tree.left.right.left.left.parent = tree.left.right.left
tree.left.right.left.right.parent = tree.left.right.left

tree.right.left = Node(1)
tree.right.left.parent = tree.right
tree.right.right = Node(4)
tree.right.right.parent = tree.right
tree.right.right.right = Node(9)
tree.right.right.right.parent = tree.right.right

print(first_common_ancestor(tree.left.right.left.left, tree.left.right.right).data)


