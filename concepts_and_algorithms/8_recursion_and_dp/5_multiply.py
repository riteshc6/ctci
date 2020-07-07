def multiply(num1: int, num2: int):
    bigger = num1 if num1 >= num2 else num2
    smaller = num1 if num1 < num2 else num2
    return _multiply(bigger, smaller)

def _multiply(bigger: int, smaller: int):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger

    # Divide smaller by 2
    s = smaller >> 1

    result = _multiply(bigger, s)

    # Multiply the result by 2    
    result <<= 1

    if smaller % 2 != 0:
        result += bigger

    return result

print(multiply(12, 14))