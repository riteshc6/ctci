import unittest

def get_mask_of_1s(j, i):
    """
        Returns (j - i + 1) 1s 
    """
    return (1 << (j - i + 1)) - 1

def get_mask_of_0s_and_1s(mask_of_1s, i):
    """
        Return series of 0s followed by i 1s
    """
    return ~(mask_of_1s << i)

def insertion(N, M, j, i):
    """
        Inser M into N from j to i bits (inclusive)
    """
    mask_of_1s = get_mask_of_1s(j, i)
    mask = get_mask_of_0s_and_1s(mask_of_1s, i)
    N = N & mask

    M = M << i
    print(bin(N | M))
    return N | M


class test_insertion(unittest.TestCase):

    data = [
        (0b10000000000, 0b10011, 6, 2, 0b10001001100),
        (0b10000000000, 0b10011, 4, 0, 0b10000010011),
        (0b10000000000, 0b10011, 10, 6, 0b10011000000)
    ]

    def test_insertion(self):
        for N, M, j, i, expected in self.data:
            actual = insertion(N, M, j, i)
            self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
