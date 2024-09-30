def find_min_operations(n, k):
    if k == 1:
        return n
    count = 0
    while n > 0:
        count += n % k
        n //= k
    return count


t = int(input())
results = []
for _ in range(t):
    n, k = map(int, input().split())
    results.append(find_min_operations(n, k))

for result in results:
    print(result)
