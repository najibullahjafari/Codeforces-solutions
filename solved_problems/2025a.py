for _ in range(int(input())):
    a = input()
    b = input()
    ans = 0
    if a in b:
        ans = len(b) + 1
    elif b in a:
        ans = len(a) + 1
    else:
        ans = len(b) + len(a)
    print(ans)
