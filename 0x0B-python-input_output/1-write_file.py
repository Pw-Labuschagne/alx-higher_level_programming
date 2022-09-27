#!/usr/bin/python3
"""This writes to a test file and returns numbers of characters written"""


def write_file(filename="", text=""):
    """Writes to text file(uft-8) and returns characters written"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
    
        x = 0
        for i in text:
            myFile.write(i)
            x +=1
        
        return x
