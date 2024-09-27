for t in range(int(input())):
    x = sorted(list(map(int, input().split())))
    # here to print the each char of x with a space between them
    print(*x)
