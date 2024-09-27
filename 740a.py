def bachgold_problem(n):
    if n % 2 == 0:
        k = n // 2
        primes = [2] * k
    else:
        k = (n // 2) - 1
        primes = [2] * k + [3]

    print(k)
    print(' '.join(map(str, primes)))


if __name__ == "__main__":
    n = int(input())
    bachgold_problem(n)
