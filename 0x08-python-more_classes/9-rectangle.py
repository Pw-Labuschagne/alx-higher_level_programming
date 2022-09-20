#!/usr/bin/python3


class Rectangle:
    """empty class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns width as private """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width value as private from user"""
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """Returns height as private """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height value as private from user"""
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """Function that returns area"""
        return self.__height * self.__width

    def perimeter(self):
        """Function that returns perimeter"""
        if (self.__height == 0 or self.__width == 0):
            return 0

        return 2 * (self.__height + self.__width)

    @classmethod
    def square(cls, size=0):
        """
        This function returns a new Rectangle instance with width=height=size
        """
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This function returns the biggest rectangle based on the area"""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')

        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')

        x = rect_1.area()
        y = rect_2.area()

        if x >= y:
            return rect_1

        else:
            return rect_2

    def __str__(self):
        """Function that prints rectangle of '#' characaters"""
        my_string = ""

        sym = str(self.print_symbol)

        if (self.__height == 0 or self.__width == 0):
            return my_string

        for i in range(self.__height):
            for j in range(self.__width):
                my_string += sym
            if (i == self.__height - 1 and j == self.__width - 1):
                break
            my_string += '\n'

        return my_string

    def __repr__(self):
        """Prints class and arguments passed to methods inside it"""
        name_string = 'Rectangle(' + str(self.__width) + ', ' \
                      + str(self.__height) + ')'
        return name_string

    def __del__(self):
        """Prints final message before an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
