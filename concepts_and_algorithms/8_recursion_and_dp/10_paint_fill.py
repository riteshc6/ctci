from enum import Enum
import random

class Color(Enum):
    Black = "B"
    White = "W"
    Red = "R"
    Yellow = "Y"
    Green = "G"

def _paint_fill(screen: list, r: int, c: int, ocolor: Color, ncolor: Color):
    if r < 0 or r >= len(screen) or c < 0 or c >= len(screen[0]):
        return False
    
    if screen[r][c] == ocolor:
        screen[r][c] = ncolor
        _paint_fill(screen, r -1, c, ocolor, ncolor)
        _paint_fill(screen, r + 1, c, ocolor, ncolor)
        _paint_fill(screen, r, c - 1, ocolor, ncolor)
        _paint_fill(screen, r, c + 1, ocolor, ncolor)
    
    return True

def paint_fill(screen: list, r: int, c: int, ncolor: Color):
    if screen[r][c] == ncolor: return False
    return _paint_fill(screen, r, c, screen[r][c], ncolor)

def print_screen(screen: list):
    for i in range(len(screen)):
        for j in range(len(screen[0])):
            print(screen[i][j], end = " ")
        print()

if __name__ == "__main__":
    n = 10
    screen = [[Color.Black]*n] * n
    
    for _ in range(20):
        screen[random.randint(0, 9)][random.randint(0, 9)] = Color.Green
    
    print_screen(screen)
    paint_fill(screen, 4, 4, Color.White)
    print("==================================================================")
    print_screen(screen)

