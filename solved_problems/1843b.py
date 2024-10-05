def max_sum_and_operations(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        max_sum = sum(abs(x) for x in a)
        operations = 0
        i = 0
        while i < n:
            if a[i] < 0:
                operations += 1
                while i < n and a[i] <= 0:
                    i += 1
            else:
                i += 1
        results.append((max_sum, operations))
    return results


t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

results = max_sum_and_operations(t, test_cases)
for result in results:
    print(result[0], result[1])
