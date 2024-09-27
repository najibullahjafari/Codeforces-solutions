for _ in range(int(input())):
    n, m, x = map(int, input().split())

    column = (x - 1) // n + 1
    row = (x - 1) % n + 1

    result = (row - 1) * m + column

    print(result)
