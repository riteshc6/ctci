class Listy:
    def __init__(self, data: list):
        self.data = data
    
    def element_at(self, i: int):
        try:
            return self.data[i]
        except IndexError:
            return -1


def search(listy: Listy, x: int):
    start = 0; end = 0

    while start <= end:
        if listy.element_at(end) == x:
            return x
        
        start = end
        end = start * 2 + 1
        if listy.element_at(end) == -1:
            while start + 1 < end and listy.element_at(end) == -1:
                end = (start + end) // 2
            if start + 1 == end:
                return -1
            return binary_search_listy(listy, x, start, end)
        elif listy.element_at(end) > x:
            return binary_search_listy(listy, x, start, end)
    return -1

def binary_search_listy(listy: Listy, x, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if listy.element_at(mid) == x:
        return x
    elif listy.element_at(mid) > x:
        return binary_search_listy(listy, x, start, mid - 1)
    else:
        return binary_search_listy(listy, x, mid + 1, end)
    

data = [2, 4, 10, 18, 24, 32, 40, 50]
listy = Listy(data)
print(search(listy, 18))
