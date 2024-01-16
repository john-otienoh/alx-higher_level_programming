#!/usr/bin/python3
def uppercase(str):
    for char in str:
        new_str = ''
        if ord(char) >= 97 and ord(char) < 123:
            char = ord(char) - 32
            new_str += chr(char)
            print("{}".format(new_str), end="")
        else:
            print("{}".format(char), end="")
