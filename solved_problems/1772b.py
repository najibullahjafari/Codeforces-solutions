for _ in range(int(input())):
    n = int(input())
    n1, n2 = map(int, input().split())
    n3, n4 = map(int, input().split())

    if n2 > n1 and n4 > n3 and n3 > n1 and n4 > n2:
        print("YES")
    else:
        # Rotate the matrix by 90 degrees
        n1, n2, n3, n4 = n3, n1, n4, n2
        if n2 > n1 and n4 > n3 and n3 > n1 and n4 > n2:
            print("YES")
        else:
            # Rotate the matrix by another 180 degrees (total 270 degrees or -90 degrees)
            n1, n2, n3, n4 = n4, n2, n3, n1
            if n2 > n1 and n4 > n3 and n3 > n1 and n4 > n2:
                print("YES")
            else:
                # Rotate the matrix by another 90 degrees (total 180 degrees or -180 degrees)
                n1, n2, n3, n4 = n3, n1, n4, n2
                if n2 > n1 and n4 > n3 and n3 > n1 and n4 > n2:
                    print("YES")
                else:
                    # Rotate the matrix by another 90 degrees (total 90 degrees or -270 degrees)
                    n1, n2, n3, n4 = n4, n2, n3, n1
                    if n2 > n1 and n4 > n3 and n3 > n1 and n4 > n2:
                        print("YES")
                    else:
                        print("NO")
