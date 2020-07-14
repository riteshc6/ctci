def merge(left: list, right: list, A: list):
    nl = len(left)
    nr = len(right)
    i = 0; j = 0; k = 0
    while i < nl and j < nr:
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1

    while i < nl:
        A[k] = left[i]
        i += 1
        k += 1

    while j < nr:
        A[k] = right[j]
        j += 1
        k += 1


def merge_sort(A: list):
    n = len(A)
    if n < 2:
        return
    
    mid = n // 2
    left, right = A[:mid], A[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, A)



A = [2, 4, 1, 6, 8, 5, 3, 7]
merge_sort(A)
print(A)