from typing import List

def bubble_sort(elems_list: List[int]):
    n = len(elems_list)

    for i in range(1, n):
        swapped = False
        for j in range(n - i):
            if elems_list[j] > elems_list[j + 1]:
                elems_list[j], elems_list[j + 1] = elems_list[j + 1], elems_list[j]
                swapped = True
        if not swapped:
            break

elems_list = [5, 1, 7, 3, 2, 6]
bubble_sort(elems_list)
print(elems_list)