from binary_search_tree import Node, in_order_traversal

def minimal_tree(array):
    """
        Returns a binary search tree with minimum height
    """
    array_length = len(array)
    # Find the index of middle element
    m = array_length // 2 if array_length % 2 else (array_length // 2) - 1
    # Initialize tree with middle element as root
    root = Node(array[m])
    # Initialize right and left indices to m, to loop in both direction from the middle of array
    right = left = m
    # Loop from the middle of the array in both direction
    for _ in range(m):
        # Right loop
        right += 1
        if right < array_length:
            root.insert(array[right])
        # left loop
        left -= 1
        if left >= 0:
            root.insert(array[left])
    return root

array = [2, 4, 6, 8 , 10, 12, 14, 18]
tree = minimal_tree(array)
in_order_traversal(tree)
print()
