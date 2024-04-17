#!/usr/bin/python3
"""Module cosnsits of class that inherits from list."""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """method that prints the sorted list """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
