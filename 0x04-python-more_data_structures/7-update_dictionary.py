#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for i, j in a_dictionary.items():
        if i == key:
            a_dictionary[i] = value
        else:
            a_dictionary.update(a_dictionary[key] = value)
    return a_dictionary
