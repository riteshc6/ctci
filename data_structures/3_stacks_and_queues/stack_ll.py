class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    

class Stack:

    def __init__(self):
        self.top = None
    
    def __str__(self):
        cur = self.top
        string = ""
        while cur:
            string += f"{cur.data} "
            cur = cur.next
        return string

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        if self.top:
            data = self.top.data
            top = self.top
            self.top = self.top.next
            top.next = None
            return data
        else:
            raise Exception("Stack is Empty")


    def peek(self):
        data = self.top.data
        return data

    def is_empty(self):
        return self.top == None

    
if __name__ == "__main__":
    data = [1,2,3,4]
    stack = Stack()
    for elem in data:
        stack.push(elem)
    while not stack.is_empty():
        print(stack.pop())