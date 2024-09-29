def is_beautiful(arr):
    total = 0
    for num in arr:
        if num == total:
            return False
        total += num
    return True


for _ in range(int(input())):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))

    if is_beautiful(l):
        print("YES")
        print(" ".join(map(str, l)))
    else:
        l.sort(reverse=True)
        if is_beautiful(l):
            print("YES")
            print(" ".join(map(str, l)))
        else:
            # Try swapping the first two elements
            l[0], l[1] = l[1], l[0]
            if is_beautiful(l):
                print("YES")
                print(" ".join(map(str, l)))
            else:
                print("NO")
