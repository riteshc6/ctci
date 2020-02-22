from binary_search_tree import Node, in_order_traversal

def minimal_tree(array):
    """
        Returns a binary search tree with minimum height
        Time Complexity = N log(N)
    """
    array_length = len(array)
    # Find the index of middle element
    m = array_length // 2 if array_length % 2 else (array_length // 2) - 1
    # Initialize tree with middle element as root
    root = Node(array[m])
    # Initialize right and left indices to m, to loop in both direction from the middle of array
    right = left = m
    # Loop from the middle of the array in both direction
    for _ in range(array_length // 2):
        # Right loop
        right += 1
        if right < array_length:
            print(array[right])
            root.insert(array[right])
        # left loop
        left -= 1
        if left >= 0:
            print(array[left])
            root.insert(array[left])
    return root


def minimal_tree_with_recursion(array, start, end):
    if end < start:
        return
    mid = (start + end) // 2
    node = Node(array[mid])
    node.left = minimal_tree_with_recursion(array, start, mid - 1)
    node.right = minimal_tree_with_recursion(array, mid + 1, end)
    return node

array = [2, 4, 6, 8 , 10, 12, 14, 18]
tree = minimal_tree(array)
in_order_traversal(tree)
print()
node = minimal_tree_with_recursion(array, 0, len(array) - 1)
in_order_traversal(node)
print()
