for _ in range(int(input())):
    a, b = map(int, input().split())
    max_num = max(a, b)
    if max_num == b:
        if (b-a) == 0 or (b-a) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
    else:
        if (a-b) == 0 or (a-b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
