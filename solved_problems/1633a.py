for _ in range(int(input())):
    n = int(input())
    up = 0
    down = 0
    ans = 0
    length_n = len(str(n))
    for c in range(length_n):
        if n % 7 == 0:
            ans = n
        else:
            n += 1
            
