for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    get_golds = 0
    count = 0
    for i in l:
        if i == 0 and count != 0:
            get_golds += 1
            count -= 1
        elif i >= k:
            count += i
    print(get_golds)
