for _ in range(int(input())):
    n = int(input())
    seq = list(map(int, input().split()))
    redsFirst = []
    redsSecond = []
    for i in range(1, n+1):
        index = i-1
        if i % 2 != 0:
            redsFirst.append(seq[index])
        elif i % 2 == 0:
            redsSecond.append(seq[index])

    a = max(redsFirst) if redsFirst else 0
    b = max(redsSecond) if redsSecond else 0
    if a >= b:
        print(a + len(redsFirst))
    else:
        print(b + len(redsSecond))
