#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8)
and returns the number of characters added"""


def append_write(filename="", text=""):
    """Appends to a file"""
    if not filename:
        with open(filename, mode="w", encoding="utf-8") as newFile:
            return newFile.write(text)
    else:
        with open(filename, mode="a", encoding="utf-8") as myFile:
            return myFile.write(text)
