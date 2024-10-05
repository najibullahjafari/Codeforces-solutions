for _ in range(int(input())):
    n = int(input())
    intgers = list(map(int, input().split()))

    if len(intgers) == 2:
        if abs(intgers[0] - intgers[1]) > 1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
