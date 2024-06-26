#!/usr/bin/python3
""" function that returns the list of available attributes and methods of an
object"""


def lookup(obj):
    """
    function that returns the list of available attributes and methods
    of an object.
    Args:
        obj (any): The object to check.
    Returns:
        list of available attributes and methods
    """
    return dir(obj)
