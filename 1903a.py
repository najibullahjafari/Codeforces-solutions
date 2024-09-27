for _ in range(int(input())):
    n, k = map(int, input().split())
    alist = list(map(int, input().split()))
    if len(alist) == k or alist == sorted(alist) or k > 1 and (len(alist)-1) == k:
        print('YES')
    else:
        mySorted = alist
        if k > 1:
            for i in range(len(mySorted) - 1):
                for j in range(0, len(mySorted) - i - 1):
                    if mySorted[j] > mySorted[j + 1]:
                        mySorted[j], mySorted[j +
                                              1] = mySorted[j + 1], mySorted[j]

        if mySorted == sorted(alist):
            print("YES")
        else:
            print('NO')
