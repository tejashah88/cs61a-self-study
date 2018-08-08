HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    return abs(street(a) - street(b)) + abs(avenue(a) - avenue(b))

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    return [int(x ** 0.5) for x in s if int(x ** 0.5) == x ** 0.5]

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    return n if n <= 3 else g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    if n <= 3:
        return n

    stack = [1, 2, 3]
    m, rindex = 4, 2
    # by using a stack to iteratively append to it, you can find the answer
    # going from 1 to n, instead of going form n to 1 in the recursive solution
    while m <= n:
        stack.append(stack[rindex] + 2 * stack[rindex - 1] + 3 * stack[rindex - 2])
        rindex += 1
        m += 1
    return stack[len(stack) - 1]

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    def helper(n, i, num, mod):
        if i == n:
            return num
        if has_seven(i) or i % 7 == 0:
            # third arg needs direct application of altered mod, due to unallowed assignment ops
            return helper(n, i + 1, num + mod * -1, mod * -1)
        else:
            return helper(n, i + 1, num + mod, mod)

    return helper(n, 1, 1, 1)


    """
    # iterative solution, illegal because of assignment ops
    mod = 1
    num = 1
    for i in range(1, n):
        if has_seven(i) or i % 7 == 0:
            mod *= -1
        num += mod
    return num
    """

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """

    def helper(amt, min_coin_value):
        if amt < 0:
            return 0
        elif amt == 0:
            return 1
        elif min_coin_value > amt:
            return 0
        else: # we either subtract min coin value from amount or double the min coin value
            return helper(amt - min_coin_value, min_coin_value) + helper(amt, min_coin_value * 2)
    return helper(amount, 1)

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """

    """
    # expanded form
    # strat: adding an extra arg to keep f in the scope
    def fn1(f):
        def fn2(k):
            return f(f, k)
        return fn2

    def fact(f, n):
        if n == 1:
            return 1
        else:
            return mul(n, f(f, sub(n, 1)))

    fn1(fact) =>
        def fn2(k): # k is the number to compute the factorial
            return fact(fact, k)

    1st expansion
        fact(fact, k) => ... return mul(n, fact(fact, sub(n, 1)))
    """

    # we use f as a reference to keep the factorial function
    return (lambda f: lambda k: f(f, k))(lambda f, n: 1 if n == 1 else mul(n, f(f, sub(n, 1))))
