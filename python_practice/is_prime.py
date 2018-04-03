"""
Define a function isPrime/is_prime() that takes one integer argument and
returns true/True or false/False depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1
that has no positive divisors other than 1 and itself.
"""


def is_prime(num):
    if num < 2:
        return '{} is not prime.'.format(num)

    for x in range(2, num):
        if int(num) % x == 0:
            return '{} is not prime.'.format(num, x)
    return '{} is prime.'.format(num)


print(is_prime(-1))
print(is_prime(13))
