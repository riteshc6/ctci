def get_magic_index_distinct(array: list)-> int:
    return _get_magic_index_distinct(array, 0, len(array) - 1)

def _get_magic_index_distinct(array: list, start: int, end: int):
    if end < start:
        return -1
    
    mid = (start + end) // 2

    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return _get_magic_index_distinct(array, start, mid - 1)
    else:
        return _get_magic_index_distinct(array, mid + 1, end)

array = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
print(get_magic_index_distinct(array))