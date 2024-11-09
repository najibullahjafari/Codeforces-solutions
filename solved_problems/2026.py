# for _ in range(int(input())):
#     x, y, k = map(int, input().split())
#     print('0', '0', x, '0')
#     print('0', '0', '0', y)

for _ in range(int(input())):
    X, Y, K = map(int, input().split())

    # Ensure the segments are within the bounds and have the required lengths
    if K <= X and K <= Y:
        Ax, Ay = 0, 0
        Bx, By = K, 0

        Cx, Cy = 0, 0
        Dx, Dy = 0, K
    else:
        # If K is greater than X or Y, we need to adjust the segments
        if K > X:
            Ax, Ay = 0, 0
            Bx, By = X, 0
        else:
            Ax, Ay = 0, 0
            Bx, By = K, 0

        if K > Y:
            Cx, Cy = 0, 0
            Dx, Dy = 0, Y
        else:
            Cx, Cy = 0, 0
            Dx, Dy = 0, 0

    print(Ax, Ay, Bx, By)
    print(Cx, Cy, Dx, Dy)
