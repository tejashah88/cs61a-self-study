def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    """BEGIN PROBLEM 2.1"""
    return m if n == 1 else m + multiply(m, n - 1)
    """END PROBLEM 2.1"""

def countdown(n):
    """
    >>> countdown(3)
    3
    2
    1
    """
    """BEGIN PROBLEM 2.2"""
    print(n)
    if n > 1:
        countdown(n - 1)
    """END PROBLEM 2.2"""

def countup(n):
    """
    >>> countup(3)
    1
    2
    3
    """
    """BEGIN PROBLEM 2.3"""
    if n > 1:
        countup(n - 1)
    print(n)
    """END PROBLEM 2.3"""

def sum_digits(n):
    """
    >>> sum_digits(7)
    7
    >>> sum_digits(30)
    3
    >>> sum_digits(228)
    12
    """
    """BEGIN PROBLEM 2.4"""
    return n % 10 + (0 if n < 10 else sum_digits(n // 10))
    """END PROBLEM 2.4"""

def count_stair_ways(n):
    """
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(3)
    3
    >>> count_stair_ways(4)
    5
    >>> count_stair_ways(5)
    8
    """
    """BEGIN PROBLEM 3.1"""
    # Hint: This is actually a slight modification of the recursive fibonacci
    # function, in that the input to output mapping is off by 1 spot
    # i.e. instead of: (2, 3, 4, 5) => (1, 2, 3, 5)
    #     we get this: (2, 3, 4, 5) => (2, 3, 5, 8)
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)
    """END PROBLEM 3.1"""

def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return sum([count_k(n - i, k) for i in range(1, k + 1)])


if __name__ == "__main__":
    import doctest
    doctest.testmod(exclude_empty=True)