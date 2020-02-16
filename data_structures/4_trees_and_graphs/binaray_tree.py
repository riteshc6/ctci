"""
    Basic Binary tree implementations
"""

class Node:
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def print_binary_tree(self):
        node = self
        print(node.data)
        left = node.left
        right = node.right
        while left or right:
            if left:
                print(left.data)
                left = node.left
            if right:
                print(right.data)
                right = node.right


tree = Node(8)
tree.left = Node(4)
tree.right = Node(10)
tree.left.left = Node(2)
tree.left.right = Node(12)
tree.right.right = Node(20)

tree.print_binary_tree()
