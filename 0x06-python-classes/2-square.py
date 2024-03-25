#!/usr/bin/python3
"""Define class Square"""


class Square:
    """
    A class Square.
    Attributes:
        __size (int): The size of the square.
    Method:
        __init__: Initializes a new Square instance.

    """
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size(int): size of the square class.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
