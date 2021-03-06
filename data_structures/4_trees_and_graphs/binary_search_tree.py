from collections import deque
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        node = self
        new_node = Node(data)
        if self.is_empty():
            node.data = data
        else:
            while node:
                
                if data <= node.data:
                    if node.left:
                        node = node.left
                    else:
                        node.left = new_node
                        break
                else:
                    
                    if node.right:
                        node = node.right
                    else:
                        node.right = new_node
                        break
        
    
    def is_empty(self):
        return self.data == None

    def search(self, value):
        if not self.data:
            raise Exception("No data in tree to serch")
        node = self
        while node:
            if node.data == value:
                return True
            node = node.left if value <= node.data else node.right
        return False

def insert_r(root, data):
    """
        Recursive method to insert in bst
    """
    if not root:
        root = Node(data)
    elif data <= root.data:
        root.left = insert_r(root.left, data)
    else:
        root.right = insert_r(root.right, data)
    return root

def search_r(root, value):
    """
        Recursive method to search bst
    """
    if not root:
        return False
    elif root.data == value:
        return True
    elif value < root.data:
        return search_r(root.left, value)
    else:
        return search_r(root.right, value)

def find_min(root):
    """
        Find minimum element in a tree
    """
    if not root:
        raise Exception("Empty Tree")
    if not root.left:
        return root.data
    else:
        return find_min(root.left)

def find_max(root):
    """
        Find maximum element in a tree
    """
    if not root:
        raise Exception("Empty tree")
    if not root.right:
        return root.data
    else:
        return find_max(root.right)

def find_height(root):
    """
        Find height of a tree
    """
    if not root:
        return -1
    return max(find_height(root.left), find_height(root.right)) + 1

def level_order_traversal(root):
    """
        Level order Traversal of a tree
    """
    if not root:
        raise Exception("Empty Tree")
    queue = deque()
    queue.append(root)
    print("Level Order Traversal: ", end=" ")
    while len(queue):
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    print()


def in_order_traversal(node):
    """
        NOTE: Space complexity = O(h); h is height of bst
    """
    if node:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)


def delete(root, data):
    """
        Deleting a node from binary search tree
    """

    if not root.data: return None

    if data < root.data:
        root.left = delete(root.left, data)
    
    elif data > root.data:
        root.right = delete(root.right, data)
    
    else:
        # Case 1: No child
        if not root.right and not root.left:
            root = None
        # Case 2: only left child
        elif not root.right:
            root = root.left
        # Case 3: only right child
        elif not root.left:
            root = root.right
        # Case 4: both right and left children are present
        else:
            min_val = find_min(root.right)  # find min value in right subtree
            root.data = min_val             # replace root with min value
            root.right = delete(root.right, root.data)  # Delete min value in right subtree

    return root
    
            
if __name__ == "__main__":
    tree = Node()
    values = [4, 10, 2, 6, 20]
    for value in values:
        tree.insert(value)
    in_order_traversal(tree)
    print()
    tree_r = None
    tree_r = insert_r(tree_r, 5)
    insert_r(tree_r, 4)
    insert_r(tree_r, 10)
    insert_r(tree_r, 2)
    insert_r(tree_r, 6)
    insert_r(tree_r, 11)
    insert_r(tree_r, 3)
    insert_r(tree_r, 1)
    in_order_traversal(tree_r)
    print()
    print(search_r(tree_r, 2))
    print(search_r(tree, 11))
    print("Minimum Element",find_min(tree_r))
    print("Maximum Element",find_max(tree_r))
    print("Height: ",find_height(tree_r))
    level_order_traversal(tree_r)
    tree_r = delete(tree_r,  5)
    level_order_traversal(tree_r)

