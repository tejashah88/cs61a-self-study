import sys
sys.path.insert(0, '../')
import test_utils
import unittest
from disc01 import *

class ProblemTester(test_utils.EnhancedTestCase):
    def test_problem_1_1(self):
        """
        >>> wears_jacket(90, False)
        False
        >>> wears_jacket(40, False)
        True
        >>> wears_jacket(100, True)
        True
        """
        self.assertEqual(wears_jacket(90, False), False)
        self.assertEqual(wears_jacket(40, False), True)
        self.assertEqual(wears_jacket(100, True), True)

    def test_problem_1_2(self):
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
        self.assertPrinted(handle_overflow, (27, 15), "No overflow")
        self.assertPrinted(handle_overflow, (35, 29), "Move to Section 2: 1")
        self.assertPrinted(handle_overflow, (20, 32), "Move to Section 1: 10")
        self.assertPrinted(handle_overflow, (35, 30), "No space left in either section")

    def test_problem_1_4(self):
        """
        >>> is_prime(10)
        False
        >>> is_prime(7)
        True
        """
        self.assertEqual(is_prime(10), False)
        self.assertEqual(is_prime(7), True)
        self.assertEqual(is_prime(35), False)
        self.assertEqual(is_prime(71), True)

    def test_problem_2_1(self):
        """Print out all integers 1..i..n where cond(i) is true
        >>> def is_even(x):
        ... # Even numbers have remainder 0 when divided by 2.
        ... return x % 2 == 0
        >>> keep_ints(is_even, 5)
        2
        4
        """
        is_even = lambda x: x % 2 == 0
        self.assertPrinted(keep_ints, (is_even, 5), "2\n4")

        is_single_digit = lambda x: x < 10
        self.assertPrinted(keep_ints, (is_single_digit, 6), "1\n2\n3\n4\n5\n6")

    def test_problem_2_3(self):
        """Returns a function which takes one parameter cond and prints out
        all integers 1..i..n where calling cond(i) returns True.
        >>> def is_even(x):
        ... # Even numbers have remainder 0 when divided by 2.
        ... return x % 2 == 0
        >>> keep_ints_compose(5)(is_even)
        2
        4
        """
        """BEGIN PROBLEM 2.3"""
        keep_ints_5 = keep_ints_compose(5)

        is_even = lambda x: x % 2 == 0
        self.assertPrinted(keep_ints_5, (is_even), "2\n4")

        is_single_digit = lambda x: x < 10
        self.assertPrinted(keep_ints_5, (is_single_digit), "1\n2\n3\n4\n5")

if __name__ == "__main__":
    unittest.main()