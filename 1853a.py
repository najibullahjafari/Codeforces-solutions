for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # 1 8 10 13
    diff = 0
    index = 0
    sorted_a = sorted(a, reverse=False)
    # print('a', a, 'sorted_a', sorted_a)
    if a == sorted_a and len(a) == 2:
        print(1)
    elif a != sorted_a:
        print(0)
    else:
        for i in range(len(a)-1):
            diff1 = a[i+1] - a[i]
            if diff1 > diff:
                diff = diff1
                index = i
            else:
                continue
        operation = -2
        while a[index+1] >= a[index]:
            a[index] += 1
            a[index+1] -= 1
            operation += 1

        print(operation)
