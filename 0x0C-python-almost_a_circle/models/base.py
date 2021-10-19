#!/usr/bin/python3
"""
    Base class
"""
import json


class Base:
    """
        This class will be the “base” of all other classes in this project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method that returns the JSON string
        representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes the JSON string representation of list_objs to a file
        """
        new_list = []
        if list_objs is not None:
            new_list = [item.to_dictionary() for item in list_objs]

        with open(cls.__name__ + ".json", "w") as new_file:
            new_file.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """
        static method that returns the list of the
        JSON string representation
        """
        pass

    @classmethod
    def create(cls, **dictionary):
        """
        class method that returns an instance with all attributes already set
        """
        pass

    @classmethod
    def load_from_file(cls):
        """
        class method that returns a list of instances
        """
        pass
