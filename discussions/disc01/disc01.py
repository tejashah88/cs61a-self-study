def wears_jacket(temp, raining):
    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    """BEGIN PROBLEM 1.1"""
    return raining or temp < 60
    """END PROBLEM 1.1"""

def handle_overflow(s1, s2):
    """
    >>> handle_overflow(27, 15)
    No overflow
    >>> handle_overflow(35, 29)
    Move to Section 2: 1
    >>> handle_overflow(20, 32)
    Move to Section 1: 10
    >>> handle_overflow(35, 30)
    No space left in either section
    """
    """BEGIN PROBLEM 1.2"""
    if max(s1, s2) < 30:
        print("No overflow")
    elif min(s1, s2) >= 30:
        print("No space left in either section")
    elif s1 > s2:
        print("Move to Section 2: %s" % (30 - s2))
    else: # s1 < s2
        print("Move to Section 1: %s" % (30 - s1))
    """END PROBLEM 1.2"""

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    """BEGIN PROBLEM 1.4"""
    if n in [2, 3]: # shortcut for if n equals 2 or 3
        return True

    if n % 2 == 0 or n < 2: # skip even numbers
        return False
    # only iterate the odd numbers from 3 to the nearest whole number of sqrt(n)
    for i in range(3, round(n ** 0.5), 2):
        if n % i == 0: # if this conditional is true, n isn't prime
            return False
    return True
    """END PROBLEM 1.4"""

def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    """BEGIN PROBLEM 2.1"""
    [print(i) for i in range(1, n + 1) if cond(i)]
    """END PROBLEM 2.1"""

def keep_ints_compose(n):
    """Returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints_compose(5)(is_even)
    2
    4
    """
    """BEGIN PROBLEM 2.3"""
    lst = [i for i in range(1, n + 1)]
    def process(cond):
        [print(i) for i in lst if cond(i)]
    return process
    """END PROBLEM 2.3"""


if __name__ == "__main__":
    import doctest
    doctest.testmod(exclude_empty=True)