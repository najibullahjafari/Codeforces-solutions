for _ in range(int(input())):
    n, m = map(int, input().split())
    x = input()
    s = input()
    indexOfs = 0
    operation = 0
    repeatedX = x * m
    if s in repeatedX:
        for c in range(m):
            if s not in x:
                x += x
                operation += 1

    if s not in repeatedX:
        print(-1)
    else:
        print(operation)
