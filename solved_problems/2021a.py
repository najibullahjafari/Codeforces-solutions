for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    i = 0
    j = 1
    evens = sorted([x for x in a if x % 2 == 0])
    odds = [x for x in a if x % 2 != 0]
    my_new_list = odds + evens
    evens.append(odds[0])
    while len(my_new_list) > 1:
        current = (my_new_list[i] + my_new_list[j])//2
        my_new_list = my_new_list[j+1:] + [current]
    print(my_new_list[0], my_new_list)
