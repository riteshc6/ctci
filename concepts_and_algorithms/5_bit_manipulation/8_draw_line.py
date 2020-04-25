
def draw_line(screen:list, w:int, x1:int, x2:int, y:int):
    bytes_per_row = w // 8
    y_index = y * bytes_per_row

    if x1 == x2:
        x_index = y_index + (x2 // 8)
        mask = (1 << (8 - (x1 % 8)))
        screen[x_index] |= mask
        return screen
    
    x1_index = x1 // 8
    x1_screen_index = y_index + x1_index
    x2_index = x2 // 8
    x2_screen_index = y_index + x2_index
    x1_bit_position = x1 % 8
    x2_bit_position = x2 % 8

    if x2_index - x1_index > 0:
        # set all bits between indexes in screen
        for i in range(x1_screen_index + 1, x2_screen_index):
            screen[i] |= 0b11111111

        # set all bits to right in current index
        screen[x1_screen_index] |= ((1 << (8 - x1_bit_position)) - 1)
        screen[x2_screen_index] |= (((1 << x2_bit_position) - 1) << (8 - x2_bit_position))
    else:
        mask = ((1 << (x2_bit_position - x1_bit_position + 1)) - 1) << (8 - x2_bit_position)
        screen[x1_screen_index] |= mask 
    return screen

screen = [255, 243, 200, 0b10101000, 0,0b00101011, 255, 255, 255]
x1 = 4; x2 = 7; w = 24; y = 1
screen = draw_line(screen, w, x1, x2, y)
print(bin(screen[3]))
x1 = 5; x2 = 24; w = 24; y = 1
screen = draw_line(screen, w, x1, x2, y)
print(bin(screen[3]))
print(bin(screen[4]))
print(screen)
