#!/usr/bin/python3
"""Module contains a function that finds a peak in
a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Function that finds a peak in a
    list of unsorted integers."""
    n = len(list_of_integers)

    if n == 0:
        return None

    if n == 1:
        return list_of_integers[0]

    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[n - 1] >= list_of_integers[n - 2]:
        return list_of_integers[n - 1]

    # Binary search to find the peak
    left = 1
    right = n - 2

    while left <= right:
        mid = (left + right) // 2

        if list_of_integers[mid] >= list_of_integers[mid - 1] and \
                list_of_integers[mid] >= list_of_integers[mid + 1]:
            return list_of_integers[mid]

        elif list_of_integers[mid - 1] > list_of_integers[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return None