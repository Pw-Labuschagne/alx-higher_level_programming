#!/usr/bin/python3
"""Now we take our Square size and give it some value"""


class Square:
    """The Square size will now take int type"""

    def __init__(self, size=0):
        try:
            self.__size = size
            return size
        except ValueError:
            print("size must be >= 0")
            return
        except TypeError:
            print("size must be an integer")
            return
