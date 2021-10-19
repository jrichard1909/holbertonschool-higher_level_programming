#!/usr/bin/python3
"""
    First Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
        class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor init"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        public method that returns the area value
        of the Rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """
        public method  prints in stdout the Rectangle
        instance with the character # - you don’t need
        to handle x and y here.
        """
        for a in range(self.__y):
            print()
        for h in range(self.__height):
            for b in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """overriding the __str__ method"""
        return("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        public method that assigns an argument
        to each attribute
        """
        if len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        public method that returns the dictionary
        representation of a Rectangle
        """
        new_dict = {}
        new_dict['x'] = self.x
        new_dict['y'] = self.y
        new_dict['id'] = self.id
        new_dict['height'] = self.height
        new_dict['width'] = self.width
        return new_dict
