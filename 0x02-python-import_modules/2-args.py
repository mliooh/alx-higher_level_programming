#!/usr/bin/env python3

import sys 

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    args_list = sys.argv[1:]

    print("Number of argument(s):", num_args, end="")
    if num_args == 0:
        print(".")
    else:
        print(":")
        for i, arg in enumerate(args_list, 1):
            print(i, ":", arg)
