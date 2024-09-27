for _ in range(int(input())):
    n = int(input())
    herelist = sorted(list(map(int, input().split())))
    total_beatuy = 0
    for c in range(len(herelist)-1, 0, -1):
        total_beatuy += herelist[c] - herelist[c-1]
    print(total_beatuy)
