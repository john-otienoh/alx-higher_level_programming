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
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
