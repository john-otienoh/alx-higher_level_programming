#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = {}
    for i, j in a_dictionary.items():
        if a_dictionary.get(i) == value:
            new_dict[i] = j
    return new_dict
