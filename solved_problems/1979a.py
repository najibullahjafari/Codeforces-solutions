def max_k_for_alice(test_cases):
    results = []
    for n, a in test_cases:
        max_val = max(a)
        second_max = float('-inf')

        # Find second max
        for num in a:
            if num > second_max and num < max_val:
                second_max = num

        # If second_max is still negative infinity, it means all elements were max_val
        # Hence, k would be max_val - 1
        if second_max == float('-inf'):
            results.append(max_val - 1)
        else:
            results.append(second_max)

    return results


# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Process and output results
results = max_k_for_alice(test_cases)
for result in results:
    print(result)
