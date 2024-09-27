for _ in range(int(input())):
    n = int(input())
    mylist = []
    num = 3
    for c in range(n*2):
        if c % 2 != 0:
            mylist.append(c)
    print(' '.join(map(str, mylist)))
