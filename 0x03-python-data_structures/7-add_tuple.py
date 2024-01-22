#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    if len(list_a) < 2:
        list_a.insert(1, 0)
        if len(list_a) < 1:
            list_a.insert(0, 0)
    if len(list_b) < 2:
        list_b.append(0)
    if len(list_b) == 0:
        list_b.append(0)
        list_b.append(0)
    tuple_a_result = list_a[0] + list_b[0]
    tuple_b_result = list_a[1] + list_b[1]
    my_new_tuple = tuple_a_result, tuple_b_result
    return my_new_tuple
