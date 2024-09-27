import math
for _ in range(int(input())):
    x, y = map(int, input().split())
    ans = math.ceil(y / 2)
    if y != 0 and y // 2 == 1:
        x -= 11
        j = x // 15
        a = ans + j
        print(a)

    else:
        i = math.ceil(y / 2)
        a = i * 7
        if x > a and i != 0:
            j = math.ceil(x / i)
            answer = i + j
            print(answer)
        else:
            print(i)
