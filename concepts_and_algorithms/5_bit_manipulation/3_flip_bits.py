
def flip_bits(num):

    string = bin(num)[2:]
    z = None
    length = 0
    max_len = 0
    for d, c in enumerate(string):

        # check for "0" and update length
        if c == "0":
            if z == None:
                z = d
                length += 1
            else:
                if length > max_len: max_len = length
                length = length - z
                z = d
        else:
            length += 1
    if length > max_len: max_len = length
    return max_len

print(flip_bits(1775))
