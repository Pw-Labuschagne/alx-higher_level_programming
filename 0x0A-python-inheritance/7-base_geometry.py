#!/usr/bin/python3
"""An empty class called BaseGeometry"""


class BaseGeometry:
    """An empty class"""
    def area(self):
        """Raises an exception for area not implemented"""
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        """Validates value
        args:
            name (string) = name
            value (int) = integer
        Raises:
            if value != integer
                TypeError: <name> must be an integer
            if value <= 0
                ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
