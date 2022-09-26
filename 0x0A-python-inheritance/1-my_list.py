#!/usr/bin/python3
"""A class which inherits from a list"""


class MyList(list):
    """Implements a function to print a list in acending order"""

    def print_sorted(self):
        """Prints list in ascending order"""
        print(sorted(self))
