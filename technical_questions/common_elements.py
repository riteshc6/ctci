A = [13, 27, 35, 40, 49, 55, 59]
B = [17, 35, 39, 40, 55, 58, 60]

length_b = len(B)
i = 0
count = 0

for elem in A:
    while i < length_b and B[i] <= elem:
        if elem == B[i]:
            count += 1
            i += 1
            break
        i += 1

print(count)

