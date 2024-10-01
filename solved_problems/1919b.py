for _ in range(int(input())):
    n = int(input())
    s = input()
    mins = 0
    plus = 0
    for c in s:
        if c == "+":
            plus += 1
        if c == '-':
            mins += 1
    print(abs(plus - mins))
