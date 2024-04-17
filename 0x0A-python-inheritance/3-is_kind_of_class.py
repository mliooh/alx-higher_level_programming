#!/usr/bin/python3
"""Module consists of a function that returns True if the object
is an instanceor else Fals.
"""


def is_kind_of_class(obj, a_class):
    """Fucntion that check of object is an instance or not.
    """
    if isinstance(obj, a_class):
        return True
    return False
