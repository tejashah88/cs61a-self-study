import sys
sys.path.insert(0, '../')
import test_utils
import unittest
from disc02 import *

class ProblemTester(test_utils.EnhancedTestCase):
    def test_problem_2_1(self):
        """
        >>> multiply(5, 3)
        15
        """
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(2, 9), 18)
        self.assertEqual(multiply(1, 1), 1)

    def test_problem_2_2(self):
        """
        >>> countdown(3)
        3
        2
        1
        """
        self.assertPrinted(countdown, (3), "3\n2\n1")
        self.assertPrinted(countdown, (6), "6\n5\n4\n3\n2\n1")

    def test_problem_2_3(self):
        """
        >>> countup(3)
        1
        2
        3
        """
        self.assertPrinted(countup, (3), "1\n2\n3")
        self.assertPrinted(countup, (6), "1\n2\n3\n4\n5\n6")

    def test_problem_2_4(self):
        """
        >>> sum_digits(7)
        7
        >>> sum_digits(30)
        3
        >>> sum_digits(228)
        12
        """
        self.assertEqual(sum_digits(7), 7)
        self.assertEqual(sum_digits(30), 3)
        self.assertEqual(sum_digits(228), 12)

    def test_problem_3_1(self):
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
        self.assertEqual(count_stair_ways(2), 2)
        self.assertEqual(count_stair_ways(3), 3)
        self.assertEqual(count_stair_ways(4), 5)
        self.assertEqual(count_stair_ways(5), 8)

    def test_problem_3_2(self):
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
        self.assertEqual(count_k(3, 3), 4)
        self.assertEqual(count_k(4, 4), 8)
        self.assertEqual(count_k(10, 3), 274)
        self.assertEqual(count_k(300, 1), 1)



if __name__ == "__main__":
    unittest.main()