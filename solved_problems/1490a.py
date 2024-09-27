for _ in range(int(input())):
    n = int(input())
    my_list = list(map(int, input().split()))

    count = 0
    for i in range(n - 1):
        a, b = my_list[i], my_list[i + 1]
        while max(a, b) > 2 * min(a, b):
            if a < b:
                a *= 2
            else:
                b *= 2
            count += 1

    print(count)
