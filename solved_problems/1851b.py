def can_sort_by_parity(n, a):
    even = [x for x in a if x % 2 == 0]
    odd = [x for x in a if x % 2 != 0]

    even.sort()
    odd.sort()

    sorted_a = []
    even_index = 0
    odd_index = 0

    for x in a:
        if x % 2 == 0:
            sorted_a.append(even[even_index])
            even_index += 1
        else:
            sorted_a.append(odd[odd_index])
            odd_index += 1

    return sorted_a == sorted(a)


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if can_sort_by_parity(n, a):
        print("YES")
    else:
        print("NO")
