"""
Define a procedure, factorial, that takes a natural number as its input, and
returns the number of ways to arrange the input number of items.
"""


def factorial(n):
    num = 1
    for x in range(n, 1, -1):
        num = num * x
    return num


print(factorial(0))  # 1
print(factorial(10))  # 3628800


# Recursive version to solve this problem
def recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(recursive(5))  # 120
