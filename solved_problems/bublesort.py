arr = [2, 3, 4, 5, 6, 1, 2, 3, 9]

for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print('sorted bubble sort:', arr)
