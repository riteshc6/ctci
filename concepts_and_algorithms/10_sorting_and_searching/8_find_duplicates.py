import random

def find_duplicates(A: list):
    bs = BitSet(32000)
    for i in range(len(A)):
        num = A[i]
        num0 = num - 1
        if bs.get(num0):
            print(num, end=" ")
        else:
            bs.set_bit(num0)
    print()

class BitSet:
    def __init__(self, size):
        self.bitset = [0] * ((size >> 5) + 1)
    
    def get(self, pos: int):
        index = pos >> 5
        bit_number = (pos & 31)
        mask = 1 << bit_number
        return self.bitset[index] & mask != 0

    def set_bit(self, pos):
        index = pos >> 5
        bit_number = (pos & 31)
        mask = 1 << bit_number
        self.bitset[index] |= mask


if __name__ == "__main__":
    A = [random.randint(1, 30) for _ in range(30)]
    print(A)
    find_duplicates(A)
