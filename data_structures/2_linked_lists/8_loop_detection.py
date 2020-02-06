from linkedlist import LinkedList, Node

def check_loop(ll):

    node_lookup = set()
    cur = ll.head

    while cur:
        if id(cur) in node_lookup:
            return cur
        node_lookup.add(id(cur))
        cur = cur.next
    
    return False


ll = LinkedList()
ll.head = Node(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6).next = ll.head

# ll.add_multiple_values([1,2,3,4,6,])
print(check_loop(ll))
