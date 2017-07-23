# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that
# is greater than the number y. 
# Then add this number z to the normal list and continue.


def numbers_in_lists(string):
    num_list = []
    i = 0
    while i < len(string):
        num_list.append(string[i])
        i += 1
    main_list = [int(num_list[0])]
    i = 0
    ref = main_list[0]
    while i < len(num_list) - 1:
        pre_list = []
        while i + 1 < len(string) and int(num_list[i + 1]) <= ref:
            pre_list.append(int(num_list[i + 1]))
            i += 1
        if pre_list:
            main_list.append(pre_list)
        while i + 1 < len(string) and int(num_list[i + 1]) > ref:
            main_list.append(int((num_list[i + 1])))
            i += 1
            ref = int(num_list[i])
    return main_list
