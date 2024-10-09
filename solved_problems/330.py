r, c = map(int, input().split())
cake = [input().strip() for _ in range(r)]

eatable_rows = [True] * r
eatable_columns = [True] * c

for i in range(r):
    if 'S' in cake[i]:
        eatable_rows[i] = False

for j in range(c):
    for i in range(r):
        if cake[i][j] == 'S':
            eatable_columns[j] = False
            break

eatable_cells = 0
for i in range(r):
    for j in range(c):
        if eatable_rows[i] or eatable_columns[j]:
            eatable_cells += 1

print(eatable_cells)
