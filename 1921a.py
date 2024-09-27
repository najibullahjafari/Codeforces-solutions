for t in range(int(input())):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    xes = [x1, x2, x3, x4]
    yes = [y1, y2, y3, y4]
    optimalY = 0
    ans = 0
    for i in range(1, 4):
        if xes[i] == x1:
            optimalY = yes[i]
    if y1 > optimalY:
        ans = y1 - optimalY
    else:
        ans = optimalY - y1
    print(ans*ans)
