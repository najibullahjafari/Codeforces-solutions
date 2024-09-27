for _ in range(int(input())):
    n = input()
    if int(n) % 2 == 0:
        print(0)
    elif len(n) == 1 and int(n) % 2 != 0:
        print(-1)
    else:
        newN = n[::-1]
        # print(newN)
        if int(newN) % 2 == 0:
            print(1)
        elif len(n) == 2 and int(n) % 2 != 0 and int(newN) % 2 != 0:
            print(-1)
        else:
            operation = 0
            odds = [2, 4, 6, 8]
            foundOdd = False
            for c in odds:
                if str(c) in n:
                    foundOdd = True

            if foundOdd:
                for i in range(len(n)-1):
                    new_n = n[:i]
                    operation += 1
                    reversed_new_n = ''.join(sorted(new_n, reverse=True))
                    if int(reversed_new_n + n[i:]) % 2 == 0:
                        break
            else:
                operation = -1
            if operation > 2:
                print(2)
            else:
                print(operation)
