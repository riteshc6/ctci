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

# For non-distinct values
def get_magic_index_repeat(array: list) -> int:
    return _get_magic_index_repeat(array, 0, len(array) - 1)

def _get_magic_index_repeat(array: list, start: int, end: int):
    if end < start:
        return -1
    
    mid_index = (start + end) // 2
    mid_value = array[mid_index]
    if mid_value == mid_index:
        return mid_index
    
    left_index = min(mid_index - 1, mid_value)
    left = _get_magic_index_repeat(array, start, left_index)
    if left >= 0:
        return left
    
    right_index = max(mid_index + 1, mid_value)
    right = _get_magic_index_repeat(array, right_index, end)
    return right
    

array = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
print(get_magic_index_distinct(array))
array2 = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
print(get_magic_index_repeat(array2))
print(get_magic_index_repeat(array))