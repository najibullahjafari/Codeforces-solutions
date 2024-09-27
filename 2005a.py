import sys
input = sys.stdin.read
output = sys.stdout.write

data = input().split()
index = 0

t = int(data[index])
index += 1
results = []

for _ in range(t):
    n = int(data[index])
    m = int(data[index + 1])
    q = int(data[index + 2])
    index += 3

    teachers = list(map(int, data[index:index + m]))
    index += m

    queries = list(map(int, data[index:index + q]))
    index += q

    # Precompute the minimum and maximum teacher positions
    min_teacher = min(teachers)
    max_teacher = max(teachers)

    # Calculate the minimum distances for each query
    for david in queries:
        min_moves = min(abs(david - min_teacher), abs(david - max_teacher))
        results.append(str(min_moves) + '\n')

output(''.join(results))
