def next_largest_number(num):
    c = num
    
    # Find c0: number of rightmost(trialing) zeros
    c0 = 0
    while ((c & 1) == 0) and (c != 0):
        c0 += 1
        c >>= 1

    # Find c1: number of rightmost(trailing) 1s
    c1 = 0
    while ((c & 1) == 1):
        c1 += 1
        c >>= 1
    
    if (c0 + c1 == 31) | (c0 + c1 == 0): return -1

    # find p: position(from right) of rightmost zero to be flipped
    p = c1 + c0

    # Set pth bit in num
    num = num | (1 << p)
    # clear all bits to the right of p
    num = num & (~((1 << p) - 1))
    # insert c1 - 1 to the right
    num = num | ((1 << (c1 - 1)) - 1)
    return num



    
def  next_smallest_number(num):
    c = num
    # find c1: number of trailing ones
    c1 = 0
    while ((c & 1) == 1):
        c >>= 1
        c1 += 1

    if c == 0: return -1

    # find c0: number trailing zeros
    c0 = 0
    while ((c & 1) == 0) and (c != 0):
        c >>= 1
        c0 += 1
    # calculate p: position of rightmost 1 before trailing 1s and 0s 
    p = c0 + c1
    # clear all bits from p + 1 to 0th bit
    num &= (-1 << (p + 1))
    # add c + 1 1s after p
    mask = ((1 << (c1 + 1)) - 1)    # sequence c1 + 1 1s
    num |= (mask << (c0 - 1))
    return num


num = 13948         # 0b11011001111100
print(bin(num), ":", bin(next_largest_number(num)))
print("0b10011110000011 :", bin(next_smallest_number(int("0b10011110000011", 2))))
