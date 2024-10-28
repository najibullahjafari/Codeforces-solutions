# for _ in range(int(input())):
#     n = int(input())
#     matrix = []
#     steps = 0
#     for _ in range(n):
#         col = list(map(int, input().split()))
#         matrix.append(col)
#     larg_num = max(max(matrix))
#     for c in range(n):
#         for r in range(n):
#             if abs(matrix[c][r]) >= larg_num:
#                 pass
#             elif matrix[c][r] < 0:
#                 steps += abs(matrix[c][r])
#     print(steps)

def main():
    t = int(input().strip())
    results = []

    for _ in range(t):
        n = int(input().strip())
        matrix = []
        for _ in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)

        steps = 0

        # Traverse the matrix and apply the magic operation
        for size in range(n, 0, -1):
            for i in range(n - size + 1):
                for j in range(n - size + 1):
                    while any(matrix[i + k][j + k] < 0 for k in range(size)):
                        for k in range(size):
                            matrix[i + k][j + k] += 1
                        steps += 1

        results.append(steps)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
