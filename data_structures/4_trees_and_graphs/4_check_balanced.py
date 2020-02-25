from collections import deque
from binary_tree import Node


def calculate_node_height(node):
    parents = [node]
    height = 0

    while parents:
        children = []
        for parent in parents:
            height += 1
            if parent.left: children.append(parent.left)
            if parent.right: children.append(parent.right)
        parents = children
    return height

def check_balanced(node):
    queue = deque()
    queue.append(node)

    while len(queue):
        root = queue.popleft()
        left_child_height = None; right_child_height = None
        if root.left:
            left_child_height = calculate_node_height(root.left)
            queue.append(root.left)

        if root.right:
            right_child_height = calculate_node_height(root.right)
            queue.append(root.right)

        if left_child_height and right_child_height:
            if abs(left_child_height - right_child_height) > 1:
                return False
        
    return True


tree = Node(8)
tree.left = Node(4)
tree.right = Node(10)
tree.left.left = Node(2)
tree.left.right = Node(6)
tree.right.left = Node(9)
tree.right.right = Node(11)
tree.right.right.right = Node(12)
tree.right.right.right.right = Node(13)

print(check_balanced(tree))


