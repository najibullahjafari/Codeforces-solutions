for _ in range(int(input())):
    n = int(input())
    s = input()
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    newword = ''
    i = n - 1
    while i >= 0:
        if s[i] == '0':
            num = int(s[i-2:i])
            newword = alphabets[num - 1] + newword
            i -= 3
        else:
            num = int(s[i])
            newword = alphabets[num - 1] + newword
            i -= 1
    print(newword)
