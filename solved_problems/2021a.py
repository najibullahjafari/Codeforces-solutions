for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    i = 0
    j = 1
    odd = [x for x in a if x % 2 != 0]
    even = [x for x in a if x % 2 == 0]
    new = odd + even

    while len(new) > 1:
        current = new[i]+new[j]
        current = current // 2
        new = new[j:] + [current]
        print(new)
        new = sorted(a)
    print(a[0])
