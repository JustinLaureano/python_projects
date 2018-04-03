"""
Find all files in the current directory where you run your code, then make a
dictionary in the following manner.

{ filename : first line of the file , ...}
"""

import os


def create_file_dict():
    file_dict = {}

    path = '.'

    files = os.listdir(path)
    for name in files:
        if os.path.isfile(name):
            file = open(name, "r")
            file_dict[name] = file.readline()

    return file_dict


print(create_file_dict())
