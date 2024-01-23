#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i in range(0, len(my_list)):
        if int(my_list[i]) % 2 == 0:
            #my_list[i] = True
            return True
        else:
            #my_list[i] = False
            return False
    #return my_list
