for _ in range(int(input())):
    n, k = map(int, input().split())
    k = sorted(list(map(int, input().split())))
    operation = 0
    for i in k[:-1]:
        operation += (i-1) + i
    print(operation)
