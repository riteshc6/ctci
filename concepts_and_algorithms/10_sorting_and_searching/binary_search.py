def binary_search(sorted_a: list, elem: int, start: int, end: int):
    if start > end:
        return -1
    
    mid = (start + end) // 2

    if sorted_a[mid] == elem:
        return elem
    elif sorted_a[mid] > elem:
        return binary_search(sorted_a, elem, 0, mid - 1)
    
    else:
        return binary_search(sorted_a, elem, mid + 1, end)

print(binary_search([5, 6, 7, 8, 9, 10, 11, 13, 15], 6, 0, 8))
