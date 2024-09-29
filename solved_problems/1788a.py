for _ in range(int(input())):
    n = int(input())
    seq = list(map(int, input().split()))

    total_product = 1
    for num in seq:
        total_product *= num

    left_product = 1

    found = False
    for k in range(1, n):
        left_product *= seq[k-1]
        right_product = total_product // left_product
        if left_product == right_product:
            print(k)
            found = True
            break

    if not found:
        print(-1)
