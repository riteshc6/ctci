def sorted_matrix_search(matrix: list, elem: int):
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:

        if matrix[row][col] == elem:
            return True
        
        elif matrix[row][col] > elem:
            col -= 1
        else:
            row += 1
    return False

if __name__ == "__main__":
    M = 10
    N = 5
    matrix = []
    for i in range(M):
        temp_array = []
        for j in range(N):
            temp = 10 * i + j
            temp_array.append(temp)
        matrix.append(temp_array)
    print(matrix)
    
    for i in range(M):
        for j in range(N):
            v = 10 * i + j
            print(str(v) + ": " + str(sorted_matrix_search(matrix, v)))
