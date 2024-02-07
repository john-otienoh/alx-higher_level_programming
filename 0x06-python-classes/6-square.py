#!/usr/bin/python3

"""A Square class"""


class Square:

    def __init__(self, size=0, position=(0,0)):
        """Initialize the square class"""

        self.__size = size
        self.__position = position

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
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    def area(self):
        """
            Public instance method that returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout"""

        for i in range(0, self.__size):
            for j in range(0, self.__size):
                if self.__size == 0:
                    print('\n')
                else:
                    print("#", end="")
            print()
