#!/usr/bin/python3
"""Now we take our Square size and give it some value"""


class Square:
    """The Square size will now take int type"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise ValueError("size must be >= 0")
        elif size < 0:
            raise TypeError("size must be an integer")
    size.__self = size
