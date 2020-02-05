from doubly_linkedlist import DoublyLinkedList

def is_palindrome(ll):
    cur = ll.head
    length = len(ll)
    tail = ll.tail
    for _ in range(length):
        if cur.data != tail.data:
            return False
        cur = cur.next
        tail = tail.prev
    return True


ll_true = DoublyLinkedList()
ll_true.append_multiple([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(is_palindrome(ll_true))
ll_false = DoublyLinkedList()
ll_false.append_multiple([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(is_palindrome(ll_false))