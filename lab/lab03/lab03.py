""" Lab 3: Recursion and Midterm Review """

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """

    # new strat: since Euclid's algorithm swaps the numbers' places for every call to gcd,
    # eventually 'b' will have no remainder, making 'a' the final answer
    return a if b == 0 else gcd(b, a % b)

    """
    old strat:
        - try to get a and b to be the bigger and smaller number, respectively
        - if a == b, then a and b are divisible by themselves, which is the gcd
        - whichever is the bigger number, if the bigger number isn't cleanly divisible by the smaller one
          call the gcp function with the new bigger number as 'a' and the smaller number as b,
          which is the remainder of the bigger divided by the smaller
        - however, if the bigger number is cleanly divisible by the smaller one, return b, which is the gcd
    """

    """
    old solution
    if a > b and a % b != 0:
        return gcd(b, a % b)
    elif b > a and b % a != 0:
        return gcd(a, b % a) # this is here to swap the bigger and smaller number role
    else:
        return b
    """

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """

    # similar to hw01, but asked for a recursive solution here
    print(n)
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(n * 3 + 1)
