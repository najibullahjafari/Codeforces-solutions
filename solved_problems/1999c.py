for _ in range(int(input())):
    n, s, m = map(int, input().split())
    time = [x for x in range(1, m)]
    bussy_tim = []
    for _ in range(n):
        l, r = map(int, input().split())
        for c in range(l, r):
            bussy_tim.append(c)
    print(time, bussy_tim)
