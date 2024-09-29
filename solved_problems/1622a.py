for _ in range(int(input())):
    l1, l2, l3 = map(int, input().split())
    listl = [l1, l2, l3]
    slist = sorted(listl)

    if sum(listl) % 2 == 0:
        if len(set(listl)) == 3:
            if slist[2] > slist[1] + slist[0]:
                print("NO")
            elif slist[2] == slist[1] + slist[0]:
                print("YES")
            else:
                print("NO")
        else:
            print("YES")

    else:
        print("NO")
    # setlist = set(listl)
    # flag = False
    # for i in range(2):
    #     if list1[i] == sum(list1[i+1:]):
    #         flag = True
    #         break
    #     else:
    #         if list1[i] == list1[i+1]:
    #             if list[i+2] % 2 == 0:
    #                 flag = True
    #                 break
    #         elif list[i] == list[i]
    # if list1[i] == list1[i+1]:
    #     if list1[i+2] % 2 == 0:
    #         flag = True
    #         break
    # elif list1[i+1] == list1[i+2]:
    #     if list1[i] % 2 == 0:
    #         flag = True
    #         break
    # elif list1[i] == list1[i+2]:
    #     if list1[i+1] % 2 == 0:
    #         flag = True
    #         break
    # else:
    #     if list1[i] != list1[i+1] and list1[i] != list1[i+2]:
    #         if list1[i+1] == list1[i+2] + list1[i]:
    #             flag = True
    #             break
    #         elif
