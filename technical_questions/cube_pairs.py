
n_range = 1, 1001

def n3_sol():
    count = 0
    for a in range(*n_range):
        for b in range(*n_range):
            for c in range(*n_range):
                # for d in range(*n_range):
                d = round(((((a ** 3) + (b ** 3)) - (c ** 3)) ** (1/3)).real)
                if (a ** 3) + (b ** 3) == (c ** 3) + (d ** 3):
                    print(a, b, c, d)
                    count += 1
    print(count)


def n2_sol():
    count = 0
    r_map = {}

    for a in range(*n_range):
        for b in range(*n_range):
            pair_sum = (a ** 3) + (b ** 3)
            if r_map.get(pair_sum):
                r_map[pair_sum].append((a, b))
            else:
                r_map[pair_sum] = [(a,b)]
    
    for result, pairs in r_map.items():
        for pair1 in pairs:
            for pair2 in pairs:
                print(*pair1, *pair2)
                count += 1
    print(count)

n2_sol()