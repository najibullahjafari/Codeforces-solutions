def main():
    t = int(input().strip())
    results = []

    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))

        # Calculate initial disturbance
        disturbance = 0
        for i in range(n - 1):
            if a[i] == a[i + 1]:
                disturbance += 1

        # Try to minimize disturbance by performing swaps
        min_disturbance = disturbance
        for i in range(n // 2):
            # Swap a[i] and a[n-i-1]
            if a[i] != a[n - i - 1]:
                # Calculate new disturbance after swap
                new_disturbance = disturbance

                # Check the effect of the swap on the disturbance
                if i > 0:
                    if a[i - 1] == a[i]:
                        new_disturbance -= 1
                    if a[i - 1] == a[n - i - 1]:
                        new_disturbance += 1
                if i < n - 1:
                    if a[i] == a[i + 1]:
                        new_disturbance -= 1
                    if a[n - i - 1] == a[i + 1]:
                        new_disturbance += 1
                if n - i - 2 >= 0:
                    if a[n - i - 2] == a[n - i - 1]:
                        new_disturbance -= 1
                    if a[n - i - 2] == a[i]:
                        new_disturbance += 1
                if n - i - 1 < n - 1:
                    if a[n - i - 1] == a[n - i]:
                        new_disturbance -= 1
                    if a[i] == a[n - i]:
                        new_disturbance += 1

                min_disturbance = min(min_disturbance, new_disturbance)

        results.append(min_disturbance)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
