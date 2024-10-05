d1, d2, d3 = map(int, input().split())
print(min((d1 + d2 + d3), (d1 + d3 << 1), (d2 + d3 << 1), d1 + d2 << 1))
