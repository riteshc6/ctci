from typing import List

def counting_sort(a: List[int]) -> list:
    k = max(a)
    aux = [0] * (k + 1)

    for elem in a:
        aux[elem] += 1

    sorted_a = []

    for i in range(k + 1):
        while aux[i] > 0:
            sorted_a.append(i)
            aux[i] -= 1
    return sorted_a

if __name__ == "__main__":
    a = [5, 2, 9, 5, 2, 3, 5]
    print(counting_sort(a))
