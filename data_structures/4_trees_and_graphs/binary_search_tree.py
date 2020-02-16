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

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)

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


tree = Node()
values = [8, 4, 10, 2, 6, 20]
for value in values:
    tree.insert(value)

tree.in_order_traversal(node=tree)
print()
print(tree.search(9))



