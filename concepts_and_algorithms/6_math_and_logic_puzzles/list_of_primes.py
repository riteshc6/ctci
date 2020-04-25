def cross_off(prime: int, flags: list, length: int) -> list:
    # starts at prime * prime because values then this would already have been crossed down
    for i in range(prime * prime, length, prime):
        flags[i] = False


def find_next_prime(prime, flags, length):
    next_ = prime + 1
    while (next_ < length) and (not flags[next_]):
        next_ += 1
    return next_


def sieve_of_eratosthenes(max_: int):
    flags = [True] * (max_ + 1)
    flags[0:2] = [False, False]
    
    prime = 2

    while prime < len(flags):
        cross_off(prime, flags, max_ + 1)
        prime = find_next_prime(prime, flags, max_ + 1)
    return flags

flags = sieve_of_eratosthenes(200)
[print(i, end=" ") for i, flag in enumerate(flags) if flag == True]
print()
