import random
try:
    size = int(input("Size ->"))
    begin = int(input("Begin ->"))
    finish = int(input("Finish ->"))
    my_list1 = list()
    my_list2 = list()
    #my_list3

    for i in range(size):
        my_list1.append(random.randint(begin, finish))
        my_list2.append(random.randint(begin, finish))

    my_list1.sort()
    my_list2.sort()

    for item in my_list1:
        print(item, end=" ")

    print()

    for item in my_list2:
        print(item, end=" ")

    print()

    my_list3 = my_list1 + my_list2
    my_list3.sort()

    for item in my_list3:  #1 task
        print(item, end=" ")

    print()


    myunique = set(my_list3)  # 2 task
    print(myunique)

    res = list(set(my_list1) & set(my_list2)) #3 task
    print(f"Sim num", res, end=" ")

    print()

    print(min(my_list1),"--", min(my_list2),"--", max(my_list1),"--", max(my_list2))




    #for item in my_list3:
        #myset = set(my_list3)
        #print(f"Duplicate {myset}")
        #break



except Exception as ex:
    print(f"Error: {ex}")