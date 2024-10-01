for _ in range(int(input())):
    n = int(input())
    s = input()
    coins = 0
    thorns = 0
    for i in range(n):
        if s[i] == '@' and thorns < 2:
            coins += 1
            thorns = 0
        elif s[i] == '*':
            thorns += 1
            # print(thorns)
        if s[i] == '.':
            thorns = 0
        if thorns >= 2:
            break

    print(coins)
    # print(thorns)
