import sys


def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        nums = list(map(int, sys.stdin.readline().strip().split()))

        unique_indexes = []
        uniques = []
        for c in nums:
            if nums.count(c) == 1:
                unique_indexes.append(nums.index(c)+1)
                uniques.append(c)

        i = 0
        for c in uniques:
            if c == min(uniques):
                break
            i += 1
        if len(unique_indexes) == 0:
            print(-1)
        else:
            print(unique_indexes[i])


if __name__ == "__main__":
    main()
