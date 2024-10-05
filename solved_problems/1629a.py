def max_ram(t, test_cases):
    results = []
    for case in test_cases:
        n, k = case['n'], case['k']
        a = case['a']
        b = case['b']

        # Pair and sort by the RAM required to run the software
        software = sorted(zip(a, b))

        current_ram = k
        for req_ram, gain_ram in software:
            if current_ram >= req_ram:
                current_ram += gain_ram

        results.append(current_ram)

    return results


# Example usage
t = 4
test_cases = [
    {'n': 3, 'k': 10, 'a': [20, 30, 10], 'b': [9, 100, 10]},
    {'n': 5, 'k': 1, 'a': [1, 1, 5, 1, 1], 'b': [1, 1, 1, 1, 1]},
    {'n': 5, 'k': 1, 'a': [2, 2, 2, 2, 2], 'b': [100, 100, 100, 100, 100]},
    {'n': 5, 'k': 8, 'a': [128, 64, 32, 16, 8], 'b': [128, 64, 32, 16, 8]}
]

results = max_ram(t, test_cases)
for result in results:
    print(result)
