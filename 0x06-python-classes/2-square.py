#!/usr/bin/python3

"""Define a class Square"""


class Square:
    "Represents a square"""

    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size(int) size of the square class
        """
        if type(int) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
