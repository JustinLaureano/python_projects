"""
Given a string with space seperated numbers, return the highest and lowest
number.
"""


def high_and_low(numbers):
    int_list = [int(number) for number in numbers.split()]
    return '{} {}'.format(max(int_list), min(int_list))


print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))  # '542, -214'
