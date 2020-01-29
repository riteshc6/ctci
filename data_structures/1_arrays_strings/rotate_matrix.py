import unittest


def matrix_rotate(array):
    N = len(array)
    rotated_array = []
    for j in range(N - 1, -1, -1):
        temp_arr = []
        for i in range(N):
            temp_arr.append(array[i][j])
        rotated_array.append(temp_arr)
    return rotated_array


class Test(unittest.TestCase):

    data = [
        # (
        #     [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
        #     [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]],
        # ),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]

    def test_rotate_matrix(self):

        for output, input_ in self.data:
            actual = matrix_rotate(input_)
            self.assertEqual(actual, output)


if __name__ == "__main__":
    unittest.main()
