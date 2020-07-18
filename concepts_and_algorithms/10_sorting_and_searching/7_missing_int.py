import array

# Bit manipulation source: https://wiki.python.org/moin/BitArrays#:~:text=If%20you%20can%20depict%20your,array%20is%20a%20natural%20choice.&text=Increasingly%20sophisticated%20modules%20are%20available,use%20a%20simple%20bit%20array.
# missing_int.txt file: https://github.com/careercup/CtCI-6th-Edition/blob/master/Java/Ch%2010.%20Sorting%20and%20Searching/Q10_07_Missing_Int/input.txt

def makeBitArray(bitSize, fill = 0):
    intSize = bitSize >> 5                   # number of 32 bit integers
    if (bitSize & 31):                      # if bitSize != (32 * n) add
        intSize += 1                        #    a record for stragglers
    if fill == 1:
        fill = 4294967295                                 # all bits set
    else:
        fill = 0                                      # all bits cleared

    bitArray = array.array('I')          # 'I' = unsigned 32-bit integer

    bitArray.extend((fill,) * intSize)

    return(bitArray)


# setBit() returns an integer with the bit at 'bit_num' set to 1.
def setBit(array_name, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    array_name[record] |= mask
    return(array_name[record])

def testBit(array_name, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31       # equivalent to bit_num % 31
    mask = 1 << offset
    return(array_name[record] & mask)


def missing_int(bit_field: list):
    with open("missing_int.txt") as f:
        for integer in f:
            setBit(bit_field, int(integer))

    for i in range(number_of_ints):
        if not testBit(bit_field, i):
            return i


if __name__ == "__main__":
    number_of_ints = 2 ** 32
    bit_field = makeBitArray(number_of_ints)
    print(missing_int(bit_field))
