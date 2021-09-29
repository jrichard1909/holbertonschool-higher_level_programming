#!/usr/bin/python3
"""module 4-square.py"""


class Square:
    """class Square that defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
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
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[1] < 0 or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):

        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                print("")
            for a in range(0, self.__size):
                for c in range(0, self.__position[0]):
                    print(" ", end="")
                for b in range(0, self.__size):
                    print("#", end="")
                print("")
