"""
Write function that subtracts all values from list a that a present in list b.
"""


def array_diff(a, b):
    return [item for item in a if item not in b]


print(array_diff([1, 2], [1, 3, 4]))  # [2] answer
