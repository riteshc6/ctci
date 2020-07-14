def insertion_sort(elems_list: list):
    n = len(elems_list)
    for i in range(1, n):
        value = elems_list[i]
        hole = i
        while hole > 0 and elems_list[hole - 1] > value:
            elems_list[hole - 1], elems_list[hole] = elems_list[hole], elems_list[hole - 1]
            hole -= 1

elems_list = [7, 2, 4, 1, 5, 3]
insertion_sort(elems_list)
print(elems_list)
a = [0, 5, 3, 2, 2]
insertion_sort(a)
print(a)
b = []
insertion_sort(b)
print(b)
c = [-2, -5, -45]
insertion_sort(c)
print(c)
