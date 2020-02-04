from linkedlist import LinkedList

def get_kth_elem(l_list, k):
    cur = l_list.head
    idx = 1
    while cur:
        if idx == k:
            return cur
        idx += 1
        cur = cur.next
    return None

def get_kth_to_last_elem(l_list, k):
    length = len(l_list)
    idx = length + 1 - k
    if l_list.head:
        cur = get_kth_elem(l_list, idx)
        if cur:
            return cur.data
        else:
            raise IndexError("Index out of range")
    else:
        return "Empty list"


l_list = LinkedList()
l_list.generate(10, 20, 30)
print(get_kth_to_last_elem(l_list,2))