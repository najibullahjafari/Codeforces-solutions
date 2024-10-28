def main():
    t = int(input().strip())
    results = []

    for _ in range(t):
        n = int(input().strip())
        matrix = [list(map(int, input().strip().split())) for _ in range(n)]

        total_steps = 0
        diagonals = {}

        for i in range(n):
            for j in range(n):
                d = i - j
                if d not in diagonals:
                    diagonals[d] = []
                diagonals[d].append(matrix[i][j])

        for d in diagonals:
            diag_values = diagonals[d]
            min_value = min(diag_values)
            if min_value < 0:
                steps_needed = -min_value
                total_steps += steps_needed
                for k in range(len(diag_values)):
                    diag_values[k] += steps_needed

        results.append(total_steps)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
