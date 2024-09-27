for _ in range(int(input())):
    a, b = map(int, input().split())
    new = a // 2
    if b % 2 == 0 and a % 2 == 0:
        print("YES")
    elif b % 2 != 0 and a % 2 != 0:
        print("NO")
    elif b % 2 != 0 and (a//2) % 2 != 0:
        print("Yes")
    elif b % 2 != 0 and a > 1 and a % 2 == 0:
        print("Yes")
    else:
        print("NO")
