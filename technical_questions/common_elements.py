array1 = [13, 27, 35, 40, 49, 55, 59]
array2 = [17, 35, 39, 40, 55, 58, 60]

i = 0
count = 0
for array1_elem in array1:
    
    for j in range(i, len(array2)):

        if array1_elem < array2[j]:
            i = j
            break
        elif array1_elem == array2[j]:
            count += 1
            i = j
            break

print(count)