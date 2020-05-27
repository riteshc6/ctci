from collections import deque
import copy
import random

class Node:
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    
    def __init__(self, root=None, child_count=0):
        self.root = root
        self.child_count = 0

    def insert(self, data):
        
        if self.root == None:
            self.root = Node(data)
        
        else:
            queue = deque()
            queue.append(self.root)
            
            while len(queue) != 0:
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                else:
                    node.left = Node(data)
                    self.child_count += 1
                    break
                
                if node.right:
                    queue.append(node.right)
                else:
                    node.right = Node(data)
                    self.child_count += 1
                    break
    
    def find(self, data):
        queue = deque()
        queue.append(self.root)

        while len(queue) != 0:
            node = queue.popleft()
            if node.data == data:
                return node
            
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return None


    def get_random_node(self):
        if self.child_count > 0:
            random_index = random.randint(1, self.child_count)
            queue = deque()
            queue.append(self.root)
            i = 1
            while i != random_index:
                node = queue.popleft()

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                i += 1
            return queue.popleft()

        else:
            return self.root


    
def bfs(tree):
    queue = deque()
    queue.append(tree)

    while len(queue) != 0:
        node = queue.popleft()
        print(node.data, end=" ")

        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    print()


tree = Tree()
node_data = [15, 8, 23, 4, 11, 19, 30, 2, 6]

for data in node_data:
    tree.insert(data)

bfs(tree.root)
print(tree.get_random_node().data)
