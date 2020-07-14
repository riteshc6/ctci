import random

def partition(A: list, start: int, end: int):
    pivot = A[end]
    p_index = start
    for i in range(start, end):
        if A[i] <= pivot:
            A[i], A[p_index] = A[p_index], A[i]
            p_index += 1
    A[p_index], A[end] = A[end], A[p_index]
    return p_index

def randomized_partition(A: list, start: int, end: int):
    pivot = random.randint(start, end)
    A[end], A[pivot] = A[pivot], A[end]
    return partition(A, start, end)

def quick_sort(A: list, start: int, end: int):
    if start < end:
        p_index = randomized_partition(A, start, end)
        quick_sort(A, start, p_index - 1)
        quick_sort(A, p_index + 1, end)


A = [7, 6, 5, 4, 3, 2, 1, 0]
quick_sort(A, 0, 7)
print(A)
