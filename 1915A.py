for c in range(int(input())):
    a, b, c = map(int, input().split())
    listNumber = [a, b, c]
    onlyOne = 0
    minnum = min(listNumber)
    for i in listNumber:
        if i == minnum:
            onlyOne += 1
    if onlyOne == 1:
        print(onlyOne)
    else:
        print(max(listNumber))
