def decode_string(encoded):
    return encoded[::-1]


t = int(input())
results = []
for _ in range(t):
    n = int(input())
    b = input().strip()
    results.append(decode_string(b))

for result in results:
    print(result)
