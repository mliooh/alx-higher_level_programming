#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_list = sorted(list(a_dictionary.keys()))
    for elem in dict_list:
        print(f"{elem}: {a_dictionary.get(elem)}")
