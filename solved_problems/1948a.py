for _ in range(int(input())):
    n = int(input())
    Alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if n <= 1:
        print("NO")
    else:

        ans = ''
        if n % 2 == 0:
            flag = True
            for c in range(n//2):
                ans += Alphabets[c] * 2
        else:
            flag = False

        if flag:
            print("YES")
            print(ans)
        else:
            print("NO")
