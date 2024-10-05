for _ in range(int(input())):
    n, k = map(int, input().split())

    found = False

    print("YES" if k % 2 == 1 and n % 2 == 1 or n % 2 == 0 else "NO")
