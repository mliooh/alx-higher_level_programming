#!/usr/bin/python3
"""
This module consists of a function that returns
the list of available attributes and methods of an object.
"""


def lookup(obj):
    """Function that returns a list of available attributes
    and methods of an object.

    Args:
        obj: Instance of the class.
    """
    return dir(obj)
