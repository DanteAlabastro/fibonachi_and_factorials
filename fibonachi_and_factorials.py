# Doing memoization using a lookup table using decorators
# That table will be just a dict.

# Convenient to put the base-cases in the lookup dict but not necessary.
# lookup = {0: 0, 1: 1}

def memoize(f):
    lookup = {}

    def helper(n):
        if n not in lookup:
            lookup[n] = f(n)
        return lookup[n]

    return helper

@memoize
def fib(n):
    """ Returns the nth Fibonacci Number.

    0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    """
    # Base cases.
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # The recursive case.
    else:
        return fib(n-1) + fib(n-2)

@memoize
def factorial(n):
    """
    Returns the factorial of n. Usually notation is n!

    Example: 5! = 5 * 4 * 3 * 2 * 1 = 120
    Example: 1! = 1, and 0! = 1
    """
    # Base cases.
    if n == 0:
        return 1
    elif n == 1:
        return 1
    # The recursive case.
    else:
        return n * factorial(n-1)
