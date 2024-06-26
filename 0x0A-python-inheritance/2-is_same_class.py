#!/usr/bin/python3
"""Checks if an object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    return True if type(obj) == a_class else False
