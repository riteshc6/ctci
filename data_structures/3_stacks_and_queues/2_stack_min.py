class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.min = None
    
    def __str__(self):
        cur = self.top
        string = ""
        while cur:
            string += str(cur.data) + " -> "
            cur = cur.next
        string += f"====== min -> {self.min}" 
        return string

    def push(self, data):
        node = Node(data)
        if not self.top:
            self.top = node
            self.min = data
        else:
            node.next = self.top
            self.top = node
            if data < self.min:
                self.min = data
    
    def pop(self):
        if not self.top:
            raise Exception("Empty stack")
        
        data = self.top.data
        self.top = self.top.next
        
        if data == self.min:
            self.update_min()
        
        return data
    
    def min_(self):
        return self.min
    
    def update_min(self):
        self.min = self.top.data
        cur = self.top

        while cur:
            if cur.data < self.min:
                self.min = cur.data
            cur = cur.next

stack = Stack()
stack.push(4)
print(stack)
stack.push(5)
print(stack)
stack.push(2)
print(stack)
stack.push(8)
print(stack)
stack.push(10)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

