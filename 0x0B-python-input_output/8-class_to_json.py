#!/isr/bin/python3
"""returns the dictionary description for JSON serialization of an object"""


def class_to_json(obj):
    """Function to return"""
    return obj.__dict__
