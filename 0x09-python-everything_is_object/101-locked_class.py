#!/usr/bin/python3
"""Defines a locked class, was documentation needed? I don't know"""


class LockedClass:
    """
    Has no class and no attributes
    Prevent the user from dynamically creating new insttancce attributes.
    """

    __slots__ = ["first_name"]
