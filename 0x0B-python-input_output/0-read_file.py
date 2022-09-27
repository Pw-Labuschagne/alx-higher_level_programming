#!/usr/bin/python3
"""Used to read a text file(UFT-8) and print to STDOUT"""


def read_file(filename=""):
    """Reads a text file UFT-8 and prints to STDOUT"""
    with open(filename,mode="r", encoding="utf-8") as myFile:

        print(myFile.read(), end="")
