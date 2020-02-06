from linkedlist import LinkedList, Node

def check_intersection(ll1, ll2):
    node_lookup = set()
    cur1 = ll1.head
    cur2 = ll2.head
    
    # populate node_lookup table with ll1 nodes
    while cur1:
        node_lookup.add(cur1)
        cur1 = cur1.next
    while cur2:
        if cur2 in node_lookup:
            return cur2
        cur2 = cur2.next
    return False

ll1 = LinkedList()
ll1.add_multiple_values([1,2,3,4,9])
ll2 = LinkedList()
ll2.add_multiple_values([5,2,3,4,9])
print(check_intersection(ll1, ll2))


