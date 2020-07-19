import sys

def sorted_valley_peaks(array: list):
    array_length = len(array)
    for i in range(1, array_length, 2):
        biggest_index = max_index(array, array_length, i - 1, i, i + 1)
        if i != biggest_index:
            array[i], array[biggest_index] = array[biggest_index], array[i]
    

def max_index(array: list, array_length: int, a: int, b: int, c: int):
    a_value = array[a] if a >= 0 and a < array_length else -sys.maxsize
    b_value = array[b] if b >= 0 and b < array_length else -sys.maxsize
    c_value = array[c] if c >= 0 and c < array_length else -sys.maxsize

    peak = max([a_value, b_value, c_value])
    if peak == a_value: return a
    if peak == b_value: return b
    if peak == c_value: return c

array = [9, 1, 0, 4, 8, 7]
sorted_valley_peaks(array)
print(array)
