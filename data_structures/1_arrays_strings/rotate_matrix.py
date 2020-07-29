import unittest

def matrix_rotate_in_place(matrix: list):
    rows = len(matrix)
    columns = len(matrix[0])

    if rows == 0 or rows != columns: return False

    for layer in range(rows//2):
        first = layer
        last = rows - 1 - layer
        for i in range(first, last):
            offset = i - first
            # save top
            top = matrix[first][i]
            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top
    
    return matrix



class Test(unittest.TestCase):

    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = matrix_rotate(test_matrix)
            print(actual)
            self.assertEqual(actual, expected)



if __name__ == "__main__":
    unittest.main()
