class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.tail = None
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def remove(self):
        if self.head:
            head = self.head
            self.head = self.head.next
            head.next = None
            return head.data
        else:
            return "Queue is empty"

    def peek(self):
        if self.tail:
            return self.tail.data
        else:
            return None

    def is_empty(self):
        return self.head == None

data = [1,2,3,4]
queue = Queue()
for elem in data:
    queue.add(elem)
while not queue.is_empty():
    print(queue.remove())