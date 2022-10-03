#!/usr/bin/python3
"""A square inherited by rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square inherited from rectangle with:
    Args:
        Size (int) = Size of sqaure
        x (int) = Called from super()
        y (int) = called from super()
        id (?) = None

    All attributes to use super() call class
    """
    
    def __init__(self, size, x=0, y=0, id=None):
        """Inherited from rectangle"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Used to return width of square"""
        return super().width

    @size.setter
    def size(self, size):
        """Used to set/get the size of the square"""
        self.width = size
        self.height = size

    def __str__(self):
        """The overloading __str__ method should return [Square] (<id>)
        <x>/<y> - <size> - in our case, width or height"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id,
                                             self.x, self.y,
                                             self.size)
    def update(self, *args, **kwargs):
        """Updates the square class through arguments:
        Args:
            1 = id
            2 = size
            3 = x
            4 = y
        **kwargs get skipped if *args exist or is not empty
        **kwargs is double pointer to dictionary: key/value
        """

        value_args = [i for i in args]
        value_kwargs = {i: kwargs[i] for i in kwargs}

        if len(value_args) > 0:

            allowed_args = ["id", "size", "x", "y"]

            args_dict = {i: c for (i, c) in zip(allowed_args, value_args)}

            if 'size' in args_dict:
                self.size = args_dict['size']

            if 'x' in args_dict:
                self.x = args_dict['x']

            if 'y' in args_dict:
                self.y = args_dict['y']

            if 'id' in args_dict:
                self.id = args_dict['id']

        if len(value_args) == 0 and len(value_kwargs) > 0:
            if 'size' in value_kwargs:
                self.size = value_kwargs['size']

            if 'x' in value_kwargs:
                self.x = value_kwargs['x']

            if 'y' in value_kwargs:
                self.y = value_kwargs['y']

            if 'id' in value_kwargs:
                self.id = (value_kwargs['id'])
    def to_dictionary(self):
        """Returns the dictionary representation of a Square
        must contain:
        id
        width
        height
        x
        y
        """

        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
