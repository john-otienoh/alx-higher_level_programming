#!/usr/bin/python3
def best_score(a_dictionary):
    a = dict(a_dictionary)
    if len(a) ==  0:
        return None
    return max(a, key=lambda i: a[i])
