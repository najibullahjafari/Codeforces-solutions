import sys
import math


def main():
    t = int(sys.stdin.readline().strip())
    results = []

    for _ in range(t):
        l, r = map(int, sys.stdin.readline().strip().split())
        x = r - l

        if x == 0:
            results.append(1)
            continue

        D = 1 + 8 * x
        k = int((-1 + math.isqrt(D)) // 2) + 1

        results.append(k)
    print("\n".join(map(str, results)))


if __name__ == "__main__":
    main()
