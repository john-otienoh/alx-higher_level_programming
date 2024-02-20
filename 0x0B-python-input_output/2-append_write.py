#!/usr/bin/python3

def append_write(filename="", text=""):
    with open(filename, 'a') as my_file:
        my_file.write(text)
    return len(text)
