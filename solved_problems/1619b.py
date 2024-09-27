for _ in range(int(input())):
    n = int(input())
    inculded_square_cubes = []
    i = 1
    if n == 1:
        print(1)
    else:
        while i**2 <= n or i**3 <= n:
            if i**2 <= n:
                inculded_square_cubes.append(i**2)
                if i**3 <= n:
                    inculded_square_cubes.append(i**3)
            i += 1
        print(len(set(inculded_square_cubes)))
