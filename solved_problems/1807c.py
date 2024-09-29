for _ in range(int(input())):
    n = int(input())
    s = input()

    char_indices = {}

    possible = True
    for i in range(n):
        if s[i] not in char_indices:
            char_indices[s[i]] = []
        char_indices[s[i]].append(i)

    for indices in char_indices.values():
        even = odd = False
        for index in indices:
            if index % 2 == 0:
                even = True
            else:
                odd = True
        if even and odd:
            possible = False
            break

    if possible:
        print("YES")
    else:
        print("NO")
