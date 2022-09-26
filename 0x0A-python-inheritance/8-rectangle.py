#!/usr/bin/python3
"""An inherited class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Now a rectangle class"""


class Rectangle(BaseGeometry):
    """Inherited from BaseGeomerty"""

    def __init__(self, width, height):
        """Instance of BaseGeometry"""
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height
