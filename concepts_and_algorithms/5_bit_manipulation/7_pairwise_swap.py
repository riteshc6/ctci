def rshift(val, n): 
    # for negative numbers from stack overflow
    return (val % 0x100000000) >> n   


def pairwise_swap(num):
    even_digits = num & 0x5555555555555555  # 64 bits for python
    odd_digits = num & 0xaaaaaaaaaaaaaaaa
    return (rshift(odd_digits, 1)) | (even_digits << 1)
x = 35
print(bin(x))
print(bin(pairwise_swap(x)))

