
def fib(n, memo):
    if n == 0: return 0
    if n == 1: return 1
    if memo[n] > 0:
        return memo[n]
    
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

memo = [0] * 10 
for i in range(10):

    print(i, ":",fib(i, memo))