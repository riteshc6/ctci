import sys

def sqrt_helper(n, min, max):

    if max < min: return -1
    
    guess = (min + max) // 2
    if guess * guess == n:
        return guess

    elif (guess * guess) < n:
        return sqrt_helper(n, guess + 1, max)
    
    else:
        return sqrt_helper(n, min, guess - 1)


def sqrt(n):
    return sqrt_helper(n, 1, n)

print(sqrt(1000))