for _ in range(int(input())):
    n, m = map(int, input().split())
    if m % 2 != 0:
        print(n*(m-1)//2)
    else:
        print((n*m)//2)
