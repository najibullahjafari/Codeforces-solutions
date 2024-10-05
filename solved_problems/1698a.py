# Read the number of test cases
t = int(input())

# Process each test case
results = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Compute the XOR of all elements in the array
    x = 0
    for num in a:
        x ^= num

    # Store the result
    results.append(x)

# Output the results
for result in results:
    print(result)
