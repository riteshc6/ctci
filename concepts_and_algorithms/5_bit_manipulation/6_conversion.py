def conversion(num1, num2):
    # xor both numbers to find bits which are different
    c = num1 ^ num2

    # count the number of bits in c
    count = 0
    while c != 0:
        count += 1
        c &= (c - 1)
    
    return count
print("89:", bin(89))
print("120:", bin(120))
print(conversion(89, 104))

