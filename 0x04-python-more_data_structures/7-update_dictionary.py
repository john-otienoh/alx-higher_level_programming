#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    my_dict = {}
    for i, j in a_dictionary.items():
        my_dict[i] = j
        if i == key:
            my_dict[i] = value
        else:
            my_dict[key] = value

    return my_dict
