from stack_ll import Stack

class MyQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    
    def __str__(self):
        string = "S1 -> "
        cur1 = self.s1.top
        while cur1:
            string += str(cur1.data) + ","
            cur1 = cur1.next
        string += "--- S2 -> "
        cur2 = self.s2.top
        while cur2:
            string += str(cur2.data)
            cur2 = cur2.next
        return string


    def push(self, data):
        self.s1.push(data)
    
    def remove(self):
        if self.s2.is_empty():
            self.reverse_stack()
        data = self.s2.pop()
        return data
    
    def peek(self):
        if self.s2.is_empty():
            self.reverse_stack()
        data = self.s2.peek()
        return data

    def reverse_stack(self):
        # Pop s1 and add it in reverse order to s2
        while not self.s1.is_empty():
            data = self.s1.pop()
            self.s2.push(data)

queue = MyQueue()
values = [1, 2, 3, 4]
for value in values:
    queue.push(value)
print(queue)

queue.remove()
print(queue)
queue.remove()
print(queue)
queue.push(8)
print(queue)
queue.push(10)
print(queue)
queue.remove()
print(queue)
queue.remove()
print(queue)
queue.peek()
print(queue)
