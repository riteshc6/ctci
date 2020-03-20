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
    
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)


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
    # print(tree.search(4))



