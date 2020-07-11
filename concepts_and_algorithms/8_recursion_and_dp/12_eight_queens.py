GRID_SIZE = 8

def place_queens(row: int, columns: list, results: list):
    if row == GRID_SIZE:
        results.append([col for col in columns])   # Creates new list object in memory and prevents overwriting
    
    else:
        for col in range(GRID_SIZE):
            if check_valid(columns, row, col):
                columns[row] = col
                place_queens(row + 1, columns, results)


def check_valid(columns: list, row1: int, column1: int):
    for row2 in range(row1):
        column2 = columns[row2]

        if column1 == column2:
            return False
        
        column_distance = abs(column2 - column1)

        row_distance = row1 - row2
        if column_distance == row_distance:
            return False
    
    return True

def print_board(columns:list):
    print("-" * (2 * GRID_SIZE + 1))
    for i in range(GRID_SIZE):
        print("|", end="")
        for j in range(GRID_SIZE):
            if columns[j] == i:
                print("Q|", end="")
            else:
                print(" |", end="")
        print()
        print("-" * (2 * GRID_SIZE + 1))
    print()


def print_boards(boards: list):
    for board in reversed(boards):
        print_board(board)

if __name__ == "__main__":
    results = []
    columns = [-1] * GRID_SIZE
    place_queens(0, columns, results)
    print_boards(results)
    print(len(results))
