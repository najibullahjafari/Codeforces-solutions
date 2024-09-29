def count_winning_starting_cities(n, deadlines):
    # Calculate the minimum time needed to conquer each city starting from the left
    min_time_needed = [0] * n
    min_time_needed[0] = deadlines[0]

    for i in range(1, n):
        min_time_needed[i] = min(min_time_needed[i-1] + 1, deadlines[i])

    # Calculate the number of winning starting cities
    winning_cities = 0
    for i in range(n):
        if min_time_needed[i] >= i + 1:
            winning_cities += 1

    return winning_cities


t = int(input())
results = []
for _ in range(t):
    n = int(input())
    deadlines = list(map(int, input().split()))
    results.append(count_winning_starting_cities(n, deadlines))

for result in results:
    print(result)
