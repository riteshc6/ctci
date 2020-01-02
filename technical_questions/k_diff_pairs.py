array = [1, 7, 5, 9, 2, 12, 3]
lookup = set(array)

k = 2

for num1 in array:
    num2 = num1 - k
    if num2 in lookup:
        print(num1, num2)

