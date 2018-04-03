"""
Write a function that takes a list as an input and prints all the items less
than 10.
"""


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def print_less_than(x):
    new_list = []

    for item in x:
        if item < 5:
            new_list.append(item)

    print(new_list)


print_less_than(a)
