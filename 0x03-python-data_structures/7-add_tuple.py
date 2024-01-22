#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        tuple_a[0] = 0
        tuple_b[0] = 0
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        tuple_a[1] = 0
        tuple_b[1] = 0
    tuple_a_result = tuple_a[0] + tuple_b[0]
    tuple_b_result = tuple_b[1] + tuple_b[1]
    my_new_tuple = tuple_a_result, tuple_b_result
    return my_new_tuple
