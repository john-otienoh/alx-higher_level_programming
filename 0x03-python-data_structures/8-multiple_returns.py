#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        my_tuple = len(sentence), None
    else:
        my_tuple = len(sentence), sentence[0]
    return my_tuple
