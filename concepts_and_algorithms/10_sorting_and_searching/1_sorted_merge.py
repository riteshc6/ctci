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

def sorted_merge_space_optimized(A: list, B: list, count_a: int, count_b: int):
    index_a = count_a - 1
    index_b = count_b - 1
    index_merged = count_a + count_b + - 1

    while index_b >= 0:
        if index_a >= 0 and A[index_a] > B[index_b]:
            A[index_merged] = A[index_a]
            index_a -= 1
        else:
            A[index_merged] = B[index_b]
            index_b -= 1
        index_merged -= 1

a = [2, 3, 4, 5, 6, 8, 10, 100, 0, 0, 0, 0, 0, 0]
b = [1, 4, 5, 6, 7, 7]
sorted_merge_space_optimized(a, b, 8, 6)
print(a)
A = [6, 7, 8, 12, 14, 0,  0, 0, 0, 0, 0, 0]
B = [2, 3, 9, 13, 15, 16, 18]
sorted_merge_space_optimized(A, B, 5, 7)
print(A)
