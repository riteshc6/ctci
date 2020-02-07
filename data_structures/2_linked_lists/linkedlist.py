from random import randint

class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
        # self.prev = prev_node
    
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.data == other.data and self.next == other.next

    def __hash__(self):
        return hash((self.data, self.next))
    

class LinkedList:

    def __init__(self):
        self.head = None
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    def __len__(self):
        length = 0
        cur = self.head
        while cur:
            length += 1
            cur = cur.next
        return length
    
    def prepend(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        return new_node
    
    def append(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
        return new_node
    
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print("")

    def add_multiple_values(self, array):

        for elem in array:
            if self.head:
                self.append(elem)
            else:
                self.head = Node(elem)
        self.print_list()
    
    def generate(self, n, min_value, max_value):
        self.head = None
        for i in range(n):
            self.append(randint(min_value, max_value))
        self.print_list()
        return self


def main():
    A = LinkedList()
    A.prepend(input("Inserting 1st at head ").strip())
    A.prepend(input("Inserting 2nd at head ").strip())
    print("\nPrint list:")
    A.print_list()
    A.append(input("\nInserting 1st at tail ").strip())
    A.append(input("Inserting 2nd at tail ").strip())
    print("\nPrint list:")
    A.print_list()
    print("\nDelete head")

if __name__ == '__main__':
    main()


