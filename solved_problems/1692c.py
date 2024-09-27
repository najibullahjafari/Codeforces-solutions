for t in range(int(input())):
    l = []
    for n in range(8):
        l.append(input())
    ans = 0
    col = 0
    row = 0
    for i in range(len(l)):
        col += 1
        for j in range(len(l)):
            if l[i][j] == '#' and l[i][j+1] == '.' and l[i][j+2] == '#':
                ans = 1
                break
