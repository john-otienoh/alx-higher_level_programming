#!/usr/bin/python3
"""Defines a Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square"""

    def __init__(self, size):
        """Intialize a new Rectangle.
        Args:
            size (int): The side of the new square
        """""
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size
        
    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
    