def minimum_bulbs(t, cases):
    results = []
    
    for k in cases:
        # Start checking from k upwards
        n = 1
        while True:
            # Count perfect squares ≤ n
            count = int(n**0.5)
            if count == k:
                results.append(n)
                break
            n += 1
            
    return results

# Input handling
t = int(input())
cases = [int(input()) for _ in range(t)]

# Output the results
results = minimum_bulbs(t, cases)
for result in results:
    print(result)
