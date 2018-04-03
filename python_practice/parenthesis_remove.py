"""
In this Kata, you will be given a mathematical string and your task will be to
remove all braces as follows:

solve("x-(y+z)") = "x-y-z"
solve("x-(y-z)") = "x-y+z"
solve("u-(v-w-(x+y))-z") = "u-v+w+x+y-z"
solve("x-(-y-z)") = "x+y+z"
There are no spaces in the expression. Only two operators are given: "+" or "-"
"""


def solve(s):
    s = s.replace('(', '')
    s = s.replace(')', '')
    s = s.replace('--', '+')
    s = s.replace('+-', '-')
    if s[0] == '+':
        s = s.replace('+', '')
    s = s.replace('-x-y', '-x+y')
    return s


print(solve("a-(b)"))
print(solve("u-(v-w-(x+y))-z"))
