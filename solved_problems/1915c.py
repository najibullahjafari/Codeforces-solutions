for t in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split()))
    num = 2
    ans = False
    if n == sum(numbers):
        print("YES")
        break
    else:
        while (num*num) <= sum(numbers):
            if n == sum(numbers):
                ans = True
                break
            if sum(numbers) == (num*num):
                ans = True
                break
            else:
                num += 1
        if ans == True:
            print("YES")
        else:
            print("NO")
