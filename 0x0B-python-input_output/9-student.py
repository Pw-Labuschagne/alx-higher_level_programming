#!/usr/bin/python3
"""Write a class Student that defines a student by"""


class student:
    """A student? Is this me?"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student with some arguments such as:
        Args:
            first_name (str) = First name
            last_name (str) = Last name
            age (int) = Age of student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """"retrieves a dictionary representation of a Student instance"""
        return self.__dict__
