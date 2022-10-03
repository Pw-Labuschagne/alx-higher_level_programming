#!/usr/bin/python3
"""Base class"""
from json import dumps, dump, loads


class Base:
    """The goal of it is to manage id attribute in all our future
    classes

    Args:
        Private class __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of
        list_dictionaries:"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation
        of list_objs to a file"""

    @staticmethod
    def from_json_string(json_string):
        """That returns the list of the JSON string
        representation json_string"""
        if json_string is None:
            return []

        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                upd = cls(1, 1)
            else:
                upd = cls(1)
            upd.update(**dictionary)
            return upd

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances:"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
