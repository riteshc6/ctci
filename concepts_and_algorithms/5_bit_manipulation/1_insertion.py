
def get_mask_of_1s(j, i):
    """
        Returns (j - i + 1) 1s 
    """
    return (1 << (j - i + 1)) - 1

def get_mask_of_0s_and_1s(mask_of_1s, i):
    """
        Return series of 0s followed by i 1s
    """
    return ~(mask_of_1s << i)

def insertion(N, M, j, i):
    """
        Inser M into N from j to i bits (inclusive)
    """
    mask_of_1s = get_mask_of_1s(j, i)
    mask = get_mask_of_0s_and_1s(mask_of_1s, i)
    N = N & mask

    M = M << i
    return N | M


N = 0b10000000000
M = 0b1011
i = 2; j = 6

print(bin(insertion(N, M, j, i)))   
