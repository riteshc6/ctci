from collections import deque
from binary_search_tree import Node


def list_of_depths(tree):
    """
        Returns list of linked lists of all elements in each level of binary tree
    """
    parents = [tree]
    depths = []

    # Initialize depths list with root of tree
    level_ll = deque([tree.data])
    depths.append(level_ll)

    # BFS traversal for each level
    while parents:
        children = []
        level_ll = deque()
        
        # Fetch all children of level and create linked list for the level
        for parent in parents:
            
            if parent.left:
                children.append(parent.left)
                level_ll.append(parent.left.data)

            if parent.right:
                children.append(parent.right)
                level_ll.append(parent.right.data)
        
        # Save current level's linked list and update parents for next level
        if children:
            depths.append(level_ll)
        parents = children
    
    return depths



tree = Node()
values = [8, 4, 10, 2, 6, 20]
for value in values:
    tree.insert(value)

depths = list_of_depths(tree)
print(depths)
