for _ in range(int(input())):
    n, m, k = map(int, input().split())
    spend = (n-1) + ((m-1)*n)
    if spend == k:
        print("YES")
    else:
        print("NO")
