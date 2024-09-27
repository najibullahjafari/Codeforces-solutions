for c in range(int(input())):
    n = int(input())
    prime = True
    if n // 2 == 0 or n // 3 == 0 or n // 5 == 0 or n // 7 == 0:
        prime = False

    if prime == True:
        print(2)
    else:
        print(n)
