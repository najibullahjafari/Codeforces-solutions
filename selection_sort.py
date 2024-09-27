arr = [2, 3, 1, 6, 5, 4, 8, 9]

for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        min_num = arr[j]

        if min_num > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print('sorted selection sort:', arr)
