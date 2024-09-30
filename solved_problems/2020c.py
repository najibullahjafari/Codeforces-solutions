def find_a(b, c, d):
    a = 0
    for i in range(62):  # Since a is in the range [0, 2^61]
        bit = 1 << i
        if (d & bit) != (b & bit) and (d & bit) != (c & bit):
            return -1
        if (d & bit) == (b & bit):
            a |= bit
    return a


t = int(input())
results = []
for _ in range(t):
    b, c, d = map(int, input().split())
    results.append(find_a(b, c, d))

for result in results:
    print(result)
