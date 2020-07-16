def search(a: list, x: int):
    return _search(a, 0, len(a) - 1, x)

def _search(a: list, left: int, right: int, x: int):
    mid = (right + left) // 2
    if x == a[mid]:
        return mid
    
    if right < left:
        return -1
    
    if a[left] < a[mid]:
        if x >= a[left] and x < a[mid]:
            return _search(a, left, mid - 1, x)
        else:
            return _search(a, mid + 1, right, x)
    elif a[mid] < a[left]:
        if x > a[mid] and x <= a[right]:
            return _search(a, mid + 1, right, x)
        else:
            return _search(a, left, mid - 1, x)
    elif a[left] == a[mid]:
        if a[mid] != a[right]:
            return _search(a, mid + 1, right, x)
        else:
            result = _search(a, left, mid - 1, x)
            if result == -1:
                return _search(a, mid + 1, right, x)
            else:
                return result
    return -1

a = [2, 3, 1, 2, 2, 2, 2, 2 , 2 , 2]
print(search(a, 2))
print(search(a, 3))
print(search(a, 4))
print(search(a, 1))
print(search(a, 8))
