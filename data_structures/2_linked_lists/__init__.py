# Represents a sequence of node, each node points to the next node
# Add/Remove items from the beggining of the list in constant time

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_head(self, data):
        newNode = Node(data)
        if self.head:
            newNode.next = self.head
        self.head = newNode
    
    def insert_tail(self, data) -> None:
        if self.head == None:
            self.insert_head(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
    
    def print_list(self) -> None:
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def delete_head(self):
        temp = self.head
        if temp:
            self.head = self.head.next
            temp.next = None
        return temp
    
    def delete_tail(self):
        temp = self.head
        if temp.next:
            while temp.next.next:
                temp = temp.next
            temp.next, temp = None, temp.next
        return temp

    def is_empty(self) -> bool:
        return self.head is None

    def reverse(self):
        current_node = self.head
        prev = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        self.head = prev

    def __repr__(self):
        current = self.head
        string = ""
        while current:
            string += f"{current} --> "
            current = current.next
        string += f"END"
        return string
    
    def __getitem__(self, index):
        current = self.head
        i = 0
        if current:
            for i in range(index + 1):
                current = current.next
            if current:
                return current
            else:
                raise IndexError("Index out of range")
        

def main():
    A = LinkedList()
    A.insert_head(input("Inserting 1st at head ").strip())
    A.insert_head(input("Inserting 2nd at head ").strip())
    print("\nPrint list:")
    A.print_list()
    A.insert_tail(input("\nInserting 1st at tail ").strip())
    A.insert_tail(input("Inserting 2nd at tail ").strip())
    print("\nPrint list:")
    A.print_list()
    A.reverse()
    print("Reversed list")
    A.print_list()
    print(A)
    print(A[5])



if __name__ == '__main__':
    main()