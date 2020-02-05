from linkedlist import LinkedList, Node
from doubly_linkedlist import DoublyLinkedList, Node as Node_d

def update_d_cur(cur):
    if cur:
        d = cur.data
        cur = cur.next
    else:
        d = 0
        return d


def sum_lists(ll1, ll2):

    llr = LinkedList()
    cur1 = ll1.head
    cur2 = ll2.head
    carry = 0
    cur_r = None
    while cur1 or cur2:
        d1 = 0; d2 = 0; sum_ = 0
        if cur1:
            d1 = cur1.data
            cur1 = cur1.next
        
        if cur2:
            d2 = cur2.data
            cur2 = cur2.next
        
        sum_ = d1 + d2 + carry
        data = sum_ % 10
        carry = sum_ // 10

        if not llr.head:
            llr.head = Node(data)
            cur_r = llr.head
        else:
            cur_r.next = Node(data)
            cur_r = cur_r.next
    return llr

def sum_lists_forward(ll1, ll2):
    cur1 = ll1.tail
    cur2 = ll2.tail
    llr = DoublyLinkedList()
    carry = 0
    cur_r = None

    while cur1 or cur2:
        d1 = 0; d2 = 0; sum_ = 0
        if cur1:
            d1 = cur1.data
            cur1 = cur1.prev
        if cur2:
            d2 = cur2.data
            cur2 = cur2.prev
        
        sum_ = d1 + d2 + carry

        carry = sum_ // 10
        data = sum_ % 10

        if not llr.tail:
            llr.tail = Node_d(data)
            cur_r = llr.tail
        else:
            cur_r.prev = Node_d(data,  next_node=cur_r)
            cur_r = cur_r.prev
    llr.head = cur_r
    return llr

ll1 = LinkedList()
ll1.add_multiple_values([7,1,6])
ll2 = LinkedList()
ll2.add_multiple_values([5,9,2])
ll = sum_lists(ll1, ll2)
ll.print_list()
ll_a = LinkedList()
ll_a.generate(4, 0, 9)
ll_b = LinkedList()
ll_b.generate(3, 0, 9)
sum_lists(ll_a, ll_b).print_list()
ll_a = DoublyLinkedList()
ll_a.append_multiple([9, 2, 7, 6])
ll_b = DoublyLinkedList()
ll_b.append_multiple([6, 7, 1])
print(sum_lists_forward(ll_a, ll_b))