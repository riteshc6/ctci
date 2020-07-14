def selection_sort(elems_list):
    n = len(elems_list)
    for i in range(n - 1):
        imin = i
        for j in range(i + 1, n):
            if elems_list[j] < elems_list[imin]:
                imin = j
        elems_list[i], elems_list[imin] = elems_list[imin], elems_list[i]

elems_list = [2, 7, 4, 1, 5, 3]
selection_sort(elems_list)
print(elems_list)
