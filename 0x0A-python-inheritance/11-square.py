#!/usr/bin/python3
"""
   Square #1
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Rectangle that inherits from BaseGeometry
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self) -> str:
        return "[Square] {}/{}".format(self.__size, self.__size)
