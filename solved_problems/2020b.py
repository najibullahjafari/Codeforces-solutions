def find_min_bulbs(k):
    return (k + 1) ** 2 - 1


t = int(input())
results = []
for _ in range(t):
    k = int(input())
    results.append(find_min_bulbs(k))

for result in results:
    print(result)
