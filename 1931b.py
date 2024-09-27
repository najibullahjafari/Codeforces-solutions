
for _ in range(int(input())):
    n = int(input())
    containers = list(map(int, input().split()))
    total_water = sum(containers)
    target = total_water // n
    possible = True
    for c in containers:
        if c > target:
            possible = False
            break
    if possible:
        print("yes")
    else:
        print("no")
