from linkedlist import LinkedList, Node

def partition(l_list, x):

    cur = l_list.head
    left_l = LinkedList()
    right_l = LinkedList()
    left_l.head = Node(x)
    left_tail = left_l.head
    while cur:
        if cur.data > x:
            right_l.prepend(cur.data)
        elif cur.data < x:
            left_node = left_l.prepend(cur.data)
        cur = cur.next
    left_tail.next = right_l.head

    l_list.head = left_l.head

ll = LinkedList()
ll.generate(10, 0, 99)
partition(ll, ll.head.data)
ll.print_list()