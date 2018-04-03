# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n - 2)


def fib(n):
    current, after = 0, 1
    for i in range(0, n):
        current, after = after, current + after
    return current


print(fibonacci(3))
print(fib(5))
