import unittest
from linkedlist import LinkedList, Node

def remove_dups(linked_list_):
    unique_elems = set()
    cur = linked_list_.head
    prev = None

    while cur:
        if cur.data in unique_elems:
            prev.next = cur.next
            cur = cur.next
        else:
            prev = cur
            unique_elems.add(cur.data)
            cur = cur.next
    return linked_list_


def remove_dups_followup(linked_list_):
    cur = linked_list_.head
    while cur:
        loop_node = cur
        while loop_node.next:
            if cur.data == loop_node.next.data:
                loop_node.next = loop_node.next.next
            else:
                loop_node = loop_node.next
        cur = cur.next
    return linked_list_


array = [8, 9, 4, 2, 9, 1, 1, 8, 5]
linked_list_ = LinkedList()
linked_list_.add_multiple_values(array)
linked_list_.print_list()
remove_dups_followup(linked_list_)
print("==================")
linked_list_.print_list()

ll = LinkedList()
ll.generate(100, 0, 9)
ll.print_list()
remove_dups_followup(ll)
print("-------------------------")
ll.print_list()



