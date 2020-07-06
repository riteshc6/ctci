def get_path(maze:list):
    maze_rows = len(maze)
    maze_cols = len(maze[0])
    if not maze or maze_rows == 0:
        return None
    path = []
    failed_points = set()

    if _get_path(maze, maze_rows - 1, maze_cols - 1, path, failed_points):
        return path
    
    return None


def _get_path(maze:list, row: int, col: int, path: list, failed_points: set):
    if row < 0 or col < 0 or not maze[row][col]:
        return False
    
    p = (row, col)

    if p in failed_points:
        return False
    
    is_at_origin = (row == 0) and (col == 0)

    if is_at_origin or _get_path(maze, row - 1, col, path, failed_points) or \
            _get_path(maze, row, col - 1, path, failed_points):
        path.append(p)
        return True
    
    failed_points.add(p)
    return False

maze = [[True, True], [False, True]]
print(get_path(maze))

