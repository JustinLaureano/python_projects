"""
Create a function that takes a list of non-negative integers and strings and
returns a new list with the strings filtered out.
"""


def filter_list(l):
    return [item for item in l if type(item) is int or type(item) is float]


print(filter_list([1, 2, 'a', 'b', 3, '4', 5, 100.0]))
