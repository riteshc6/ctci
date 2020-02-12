class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.state_min = []
        # self.cur_state = None
    
    def __str__(self):
        cur = self.top
        string = ""
        if self.top:
            while cur:
                string += str(cur.data) + " -> "
                cur = cur.next
            string += f"====== min -> {self.min()}" 
        return string

    def push(self, data):
        node = Node(data)
        if not self.top:
            self.top = node
            self.cur_state = 0
            self.state_min.append(data)
        else:
            node.next = self.top
            self.top = node
            self.cur_state += 1
            if data < self.state_min[- 1]:
                self.state_min.append(data)
    
    def pop(self):
        if not self.top:
            raise Exception("Empty stack")
        
        data = self.top.data
        self.top = self.top.next
        
        if data == self.state_min[-1]:
            self.state_min.pop(-1)
        
        return data
    
    def min(self):
        return self.state_min[-1]


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
stack.pop()
print(stack)


