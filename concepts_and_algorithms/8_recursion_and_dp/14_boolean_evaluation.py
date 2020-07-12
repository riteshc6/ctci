from typing import Dict

def string_to_bool(string: str):
    return False if string == "0" else True

def count_eval(s: str, result: bool, memo: Dict[str, int]):
    string_length = len(s)
    if string_length == 0: return 0
    if string_length == 1: return 1 if string_to_bool(s) == result else 0
    if memo.get(str(result) + s):
        return memo.get(str(result) + s)
    ways = 0

    for i in range(1, string_length, 2):
        c = s[i]
        left = s[:i]
        right = s[i + 1:]
        left_true = count_eval(left, True, memo)
        left_false = count_eval(left, False, memo)
        right_true = count_eval(right, True,  memo)
        right_false = count_eval(right, False, memo)
        total = (left_true + left_false) * (right_true + right_false)

        total_true = 0
        if c == "^":
            total_true = left_true * right_false + left_false * right_true
        elif c == "&":
            total_true = left_true  * right_true
        elif c == "|":
            total_true = left_true * right_true + left_false * right_true + left_true * right_false

        sub_ways = total_true if result else total - total_true

        ways += sub_ways

    memo[str(result) + s] = ways
    return ways

expression = "0^0|1&1^1|0|1"
result = True
memo = {}
print(count_eval(expression, result, memo))
