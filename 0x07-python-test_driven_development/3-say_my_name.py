#!/usr/bin/python3
"""Defines a name printing funtion."""


def say_my_name(first_name, last_name=""):
    """ Prints my name is <first name> <last name>.

    Raises:
        TypeError: If either of first_name or last_name is not a string.
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
