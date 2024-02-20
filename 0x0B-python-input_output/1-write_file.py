#!/usr/bin/python3

def write_file(filename="", text=""):
    """
        Function that writes a string to a text file (UTF8)
        Returns the number of characters written
    """
    with open(filename, 'w') as my_file:
        my_file.write(text)
    return len(text)
