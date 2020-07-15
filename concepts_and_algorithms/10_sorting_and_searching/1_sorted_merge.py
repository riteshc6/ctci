def sorted_merge(A: list, B: list):
    len_a = len(A)
    len_b = len(B)

    A_slice = A[:len_a - len_b]
    merge(A, A_slice, B)
    return A

def merge(A, left: list, right: list):
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
        k += 1; i += 1
    
    while j < nr:
        A[k] = right[j]
        k += 1; j += 1
    
A = [6, 7, 8, 12, 14, None,  None, None, None, None, None, None]
B = [2, 3, 9, 13, 15, 16, 18]
print(sorted_merge(A, B))

