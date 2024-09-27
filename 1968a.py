def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for _ in range(int(input())):
    n = int(input())
    if n <= 2:
        print(1)

    elif n % 2 == 0:
        print(n-2)
    else:
        odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        reversed_odds = odds[::-1]
        if n in primes:
            print(n-1)
        else:
            ans = 0
            for i in range(1, 19):
                if n % i == 0:
                    ans = n-i
                    break
            print(ans)
