from linkedlist import LinkedList, Node
import copy

def del_mid_node(node):
    """
        NOTE: The previous node will be pointing to current object, thus we have to modify current object's elements' values
    """
    if node == None or node.next == None:
        return False
    
    node.data = node.next.data
    node.next = node.next.next
    return True


ll = LinkedList()
ll.add_multiple_values([1, 2, 3, 4])
middle_node = ll.append(5)
ll.add_multiple_values([7, 8, 9])

ll.print_list()
deleted = del_mid_node(middle_node)
if deleted:
    ll.print_list()
else:
    print("Not a valid node")
