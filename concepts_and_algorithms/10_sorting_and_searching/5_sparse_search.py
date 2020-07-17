def sparse_search(A: list, word: str):
    start = 0
    end = len(A) - 1
    return binary_search(A, word, start, end)


def binary_search(A: list, word: str, start: int, end: int):
    if start > end: return -1

    mid = (start + end) // 2

    if A[mid] == word:
        return mid
    
    if A[mid] == "":
        mid = find_non_empty_mid(A, mid, start, end)
        if mid == -1:
            return  -1

        if A[mid] == word:
            return mid
        if word < A[mid]:
            return binary_search(A, word, start, mid - 1)
        else:
            return binary_search(A, word, mid + 1, end)

    if word < A[mid]:
        return binary_search(A, word, start, mid - 1)
    else:
        return binary_search(A, word, mid + 1, end)


def find_non_empty_mid(A: list, mid: int, start: int, end: int):
    left_index = mid - 1
    right_index = mid + 1

    while start <= left_index < mid or mid < right_index <= end:
        if A[left_index]:
            return left_index
        left_index -= 1

        if A[right_index]:
            return right_index
        right_index -= 1
    return -1

A = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
print(sparse_search(A, "ball"))
