from linkedlist import LinkedList, Node

def check_loop_using_lookup(ll):

    node_lookup = set()
    cur = ll.head

    while cur:
        if id(cur) in node_lookup:
            return cur
        node_lookup.add(id(cur))
        cur = cur.next
    
    return False

def check_loop(ll):
    slow = ll.head
    fast = ll.head

    # Moves fast K steps near to corrupt node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast is slow:
            break
    
    if not fast or not fast.next:
        return None
    
    slow = ll.head
    # Both slow and fast are k steps away from corrupt node
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow


ll = LinkedList()
ll.head = Node(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6).next = ll.head

# ll.add_multiple_values([1,2,3,4,6,])
print(check_loop_using_lookup(ll))
print(check_loop(ll))
