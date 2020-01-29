import unittest

def zero_matrix(matrix):
    row = set()
    column = set()
    m = len(matrix); n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row.add(i)
                column.add(j)
    for i in range(m):
        if i in row:
            matrix[i] = [0] * n
            continue
        for j in range(m):
            if j in column:
                matrix[i][j] = 0
    return matrix

class Test(unittest.TestCase):

    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]
    
    def test_zero_matrix(self):

        for input_, expected in self.data:
            actual = zero_matrix(input_)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
