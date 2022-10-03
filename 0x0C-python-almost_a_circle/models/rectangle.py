#!/usr/bin/python3
"""A rectangle that inherits from base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle with private attributes and own public getter 
    and setter
    Args:
        __Width (int) = Width of rectangle
        __height (int) = Height of rectangle
        __x (int) = Width of rectagle?
        __y (int) = Height of rectangle?
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns the witdh value as private"""
        return self.__width
        
    @width.setter
    def width(self, width):
        """Sets the width value as private
        Raises:
            TypeError = Value not int
            ValueError = Value > 0
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """Returns the height value as private"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets height value as private
        Raises:
            TypeError = Value not int
            ValueError = Value <= 0
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        """Returns x as private value"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets x value as private
        Raises:
            TypeError = Value not int
            ValueError = Value < 0
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        """Returns y as private value"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets y value as private
        Raises:
            TypeError = Value not int
            ValueError = Value < 0
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """Returns the value of Rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """Print function for rectangle"""
        if self.__y > 0:
            for a in range(self.__y):
                print()

        for i in range(self.__height):
            if self.__x > 0:
                for b in range(self.__x):
                    print(' ', end="")
                
            for c in range(self.__width):
                if i == self.__height - 1 and c == self.__width - 1:
                    print("#")
                    break
                if c == self.__width - 1:
                    print("#")
                    continue
                    
                print("#", end="")
    def __str__(self):
        """Update the class Rectangle by overriding the __str__ method
        so that it returns [Rectangle] (<id>) <x>/<y> -
        <width>/<height>"""

        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id,
                                                self.x, self.y,
                                                self.width,
                                                self.height)

    def update(self, *args, **kwargs):
        """Updates the rectangle class through arguments:
        Args:
            1 = id
            2 = width
            3 = height
            4 = x
            5 = y
        **kwargs get skipped if *args exist or is not empty
        **kwargs is double pointer to dictionary: key/value
        """

        value_args = [i for i in args]
        value_kwargs = {i: kwargs[i] for i in kwargs}

        if len(value_args) > 0:

            allowed_args = ["id", "width", "height", "x", "y"]

            args_dict = {i: c for (i, c) in zip(allowed_args, value_args)}

            if 'width' in args_dict:
                self.width = args_dict['width']

            if 'height' in args_dict:
                self.height = args_dict['height']

            if 'x' in args_dict:
                self.x = args_dict['x']

            if 'y' in args_dict:
                self.y = args_dict['y']

            if 'id' in args_dict:
                super().__init__(args_dict['id'])

        if len(value_args) == 0 and len(value_kwargs) > 0:
            if 'width' in value_kwargs:
                self.width = value_kwargs['width']

            if 'height' in value_kwargs:
                self.height = value_kwargs['height']

            if 'x' in value_kwargs:
                self.x = value_kwargs['x']

            if 'y' in value_kwargs:
                self.y = value_kwargs['y']

            if 'id' in value_kwargs:
                super().__init__(value_kwargs['id'])



    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle
        must contain:
        id
        width
        height
        x
        y
        """

        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
