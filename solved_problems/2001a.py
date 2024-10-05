for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    if len(l) == len(set(l)):
        print(n-1)
    else:
        more = l.count(l[0])
        more_c = 0

        for c in l:
            if l.count(c) > more:
                more = l.count(c)
                more_c = c
        newarr = []
        ans = 0
        for c in l:
            if c != more_c:
                ans += 1

        print(ans)
