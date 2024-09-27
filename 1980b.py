for t in range(int(input())):
    n, f, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    favorite_cube = numbers[f-1]
    reverse_number = sorted(numbers, reverse=True)
    current_number = reverse_number[k:] if k < len(reverse_number) else []
    if len(set(current_number)) < len(current_number):
        print('maybe')
    elif favorite_cube in current_number:
        print('No')
    else:
        print('yes')
