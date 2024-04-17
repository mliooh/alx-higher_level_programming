#!/usr/bin/python3
"""
Module consists of a function that checks if
the object is an instance of a class that inherited from the
specified class.
"""


def inherits_from(obj, a_class):
    """Function that checks if object is an instance of a class
    that inherited from the specified class.

    Args:
        obj: object
        a_class: class type

    Returns:
        True if obj is an instance of a_class
        False otherwise.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
