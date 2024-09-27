# for _ in range(int(input())):
#     n = int(input())
#     letters = set(input())

#     upperalphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     ans = 0
#     loopedLetters = []
#     for c in letters:
#         indexOFCharC = upperalphabet.index(c)+1

#         if n >= ((sum(loopedLetters) + indexOFCharC)):
#             ans += 1
#             n -= indexOFCharC
#             loopedLetters.append(indexOFCharC)

#     print(ans)

for _ in range(int(input())):
    n = int(input())
    log = input()

    time_spent = {}
    for c in log:
        if c in time_spent:
            time_spent[c] += 1
        else:
            time_spent[c] = 1

    solved_problems = 0
    for c in time_spent:
        required_time = ord(c) - ord('A') + 1
        if time_spent[c] >= required_time:
            solved_problems += 1

    print(solved_problems)
