def count_ways(n: int):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)

def count_ways_memo(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo.get(n):
        return memo[n]

    memo[n]= count_ways_memo(n - 1, memo) + count_ways_memo(n - 2, memo) + count_ways_memo(n - 3, memo)
    return memo[n]

print(count_ways(5))
print(count_ways_memo(10, {}))


