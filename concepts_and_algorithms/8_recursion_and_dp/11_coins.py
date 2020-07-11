def _make_change(amount: int, denoms: list, index: int, memo: dict):
    if memo.get((amount, index)):
        return memo[(amount, index)]
    if index >= len(denoms) - 1: return 1
    denom_amount = denoms[index]
    ways = 0

    i = 0
    while i * denom_amount <= amount:
        amount_remaining = amount - i * denom_amount
        ways += _make_change(amount_remaining, denoms, index + 1, memo)
        i += 1
    memo[(amount, index)] = ways
    return ways

def make_change(n: int):
    denoms = [25, 10, 5, 1]
    memo = {}
    return _make_change(n, denoms, 0, memo)

print(make_change(100))