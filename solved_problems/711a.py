t = int(input())
flag = False
sets = False
zs = []
for c in range(t):
    pairs = list(map(str, input().split('|')))
    if 'OO' in pairs and sets == False:
        flag = True
        if pairs[0] == 'OO':
            pairs[0] = '++'
            zs.append(pairs)
            sets = True
        else:
            pairs[1] = '++'
            zs.append(pairs)
            sets = True
    else:
        zs.append(pairs)

if flag:
    print("YES")
    for pair in zs:
        print('|'.join(pair))
else:
    print("NO")
    # for pair in zs:
    #     print('|'.join(pair))
