#!/usr/bin/python3

"""A Square class"""


class Square:

    def __init__(self, size=0):
        """Initialize the square class"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value    
    def area(self):
        """
            Public instance method that returns the current square area
        """
        return self.__size ** 2
