""" Optional problems for Lab 3 """

from lab03 import *

## Higher order functions

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """

    # very nice duplicate (lab02 extra problems)
    def init_cycle(n):
        if n == 0:
            return lambda i: i
        else:
            arr = [f1, f2, f3]
            def composed(start):
                for i in range(1, n + 1):
                    start = arr[(i - 1) % 3](start)
                return start
            return composed
    return init_cycle

## Lambda expressions

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """

    """
    strat:
      - 'x' and 'y' are effectively inversly proportional
      - 'f' should use x and y somehow
      - the idea is to ideally rebuild the palindrome in 'y' backwards;
        pop the ones digit of x and push into 'y' from the right side
      - actual strat: effectively reverse the digits numerically this way and comparing
        it to the original number
    """
    x, y = n, 0
    f = lambda: y * 10 + x % 10
    while x > 0:
        x, y = x // 10, f()
    return y == n

## More recursion practice

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2:
        return n
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def no_divisors(n, k):
        if n < 2:
            return False
        if k == 1:
            return True
        else:
            if n % k == 0:
                return False
            else:
                return no_divisors(n, k - 1)
        return True

    return no_divisors(n, n - 1)


def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    if n == 1:
        return odd_term(1)
    return (odd_term(n) if n % 2 == 1 else even_term(n)) + interleaved_sum(n - 1, odd_term, even_term)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """

    def count_digits(n, d):
        if n < 10:
            return int(n == d)
        if n % 10 == d:
            return 1 + count_digits(n // 10, d)
        else:
            return count_digits(n // 10, d)

    def helper(n):
        if n < 10:
            return 0
        else:
            # we don't pass 'n' directly, to avoid counting the ones digit
            return count_digits(n // 10, 10 - n % 10) + helper(n // 10)
    return helper(n)

    """
    old solution - had assignment ops which were illegal for this question
    count = 0
    for m in range(1, 5):
        t1, t2 = count_digits(n, m), count_digits(n, 10 - m)
        if min(t1, t2) != 0:
            count += t1 * t2

    t3 = count_digits(n, 5)
    if t3 > 1:
        count += factorial(t3 - 1)
    """

    return count
