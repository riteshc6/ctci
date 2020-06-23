def fib_iter_bottom_up(n):
    prev = 1
    next_ = 1
    i = 1
    print(prev,  end=" ")
    while i < 10:
        print(next_, end=" ")
        prev, next_ = next_, prev + next_
        i += 1
    print()
    return prev

def fib_recur(n: int):
    if n == 0: return 0
    if n == 1: return 1

    return fib_recur(n - 1) + fib_recur(n - 2)

def fib_recur_memo(n: int, memo: dict):
    if n == 0 or n == 1: return n
    if not memo.get(n):
        return fib_recur_memo(n - 1, memo) + fib_recur_memo(n - 2, memo)
    return memo[n]



print(fib_iter_bottom_up(10))
f = fib_recur(10)
print(f)
print(fib_recur_memo(10, {}))