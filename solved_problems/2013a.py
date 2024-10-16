for _ in range(int(input())):
    n = int(input())
    x, y = map(int, input().split())
    steps = 0
    mn = min(x, y)
    if n % mn == 0:
        print(n // mn)
    else:
        print((n // mn)+1)
