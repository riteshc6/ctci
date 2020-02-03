class Node:

    def __init__(self, data, next_node = None, prev_node = None):
        self.data = data
        self.next = next_node
        self.prev = prev_node
    
    def __str__(self):
        return str(self.data)

    
class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def __str__(self):

        values = [str(node) for node in self]
        return " -> ".join(values)


    def __len__(self):
        length = 0
        cur = self.head
        while cur:
            length += 1
            cur = cur.next
        return length

    def prepend(self, data):
        if self.head:
            self.head = self.prev = Node(data, next_node=self.head)
        else:
            self.head = self.tail = Node(data)
        return self.head

    def append(self, data):
        if self.tail: 
            self.tail.next = Node(data, prev_node=self.tail)
            self.tail = self.tail.next
        else:
            self.head = self.tail = Node(data)
        return self.tail

    def append_multiple(self, values):
        for value in values:
            self.append(value)

        


def main():
    A = DoublyLinkedList()
    A.prepend(input("Inserting 1st at head ").strip())
    A.prepend(input("Inserting 2nd at head ").strip())
    print("\nPrint list:")
    print(A)
    A.append(input("\nInserting 1st at tail ").strip())
    A.append(input("Inserting 2nd at tail ").strip())
    print("\nPrint list:")
    print(A)
    A.append_multiple(([10,11,12,1434]))
    print(A)

if __name__ == '__main__':
    main()