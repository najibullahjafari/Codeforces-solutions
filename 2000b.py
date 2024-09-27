for _ in range(int(input())):
    n = int(input())
    seats = list(map(int, input().split()))
    occupied = set()
    valid = True

    for i in range(n):
        seat = seats[i]
        if i > 0:
            if (seat - 1 not in occupied) and (seat + 1 not in occupied):
                valid = False
                break
        occupied.add(seat)

    if valid:
        print("YES")
    else:
        print("NO")
