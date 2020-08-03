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


def get_tail_and_size(ll):
    tail = None
    size = 0
    while ll:
        size += 1
        if ll.next:
            ll = ll.next
        else:
            tail = ll
            break
    return tail, size

def get_kth_node(ll, k):
    if not ll:
        raise Exception("Empty linked list")
    for _ in range(k):
        ll = ll.next
    return ll

def get_intersection(ll1, ll2):
    ll1 = ll1.head
    ll2 = ll2.head
    tail1, size1 = get_tail_and_size(ll1)
    tail2, size2 = get_tail_and_size(ll2)

    if tail1.data != tail2.data:
        return False
    
    if size1 > size2:
        ll1 = get_kth_node(ll1, size1 - size2)
    elif size1 < size2:
        ll2 = get_kth_node(ll2, size2 - size1)
    
    while ll1 and ll2:
        if ll1.data == ll2.data:
            return ll1
        ll1 = ll1.next
        ll2 = ll2.next


ll1 = LinkedList()
ll1.add_multiple_values([1,2,3,4,9])
ll2 = LinkedList()
ll2.add_multiple_values([5,2,3,4,9])
print(get_intersection(ll1, ll2).data)


