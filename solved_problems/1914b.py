for _ in range(int(input())):
    n, k = map(int, input().split())
    coming_list = sorted([x for x in range(1, n+1)], reverse=True)
    coming_list[-k-1:] = reversed(coming_list[-k-1:])

    print(' '.join(map(str, coming_list)))
