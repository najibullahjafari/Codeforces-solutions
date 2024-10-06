for _ in range(int(input())):
    n, k = map(int, input().split())
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    my_alpha = alphabets[:k]
    my_str = ''
    ans_str = ''

    for i in range(k):
        my_str = my_str + alphabets[i]
    print(my_str * n)
