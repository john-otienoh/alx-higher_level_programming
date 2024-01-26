#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dicionary) ==  0:
        return None
    else:
        my_list = list(a_dictionary.values())
        largest_value = my_list[0]
        for i in len(my_list):
            if my_list[i] > largest_value:
                largest_value = my_list[i]

