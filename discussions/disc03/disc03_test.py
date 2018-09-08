import sys
sys.path.insert(0, '../')
import test_utils
import unittest
from disc03 import *

t = tree(1,
         [tree(3,
               [tree(4),
                tree(5),
                tree(6)]),
          tree(2)])

s = tree(11,
         [tree(32,
               [tree(4),
                tree(15,
                     [tree(21),
                      tree(45)]),
                tree(8)]),
          tree(2,
               [tree(12),
                tree(2)])])

u = tree(2,
         [tree(7,
               [tree(3),
                tree(6,
                     [tree(5),
                      tree(11)])]),
          tree(15)])

squared_t = tree(1,
                 [tree(9,
                       [tree(16),
                        tree(25),
                        tree(36)]),
                  tree(4)])

class ProblemTester(test_utils.EnhancedTestCase):
    def test_problem_3_1(self):
        """Return the max of a tree
        >>> t = tree(1,
        ...          [tree(3,
        ...                [tree(4),
        ...                 tree(5),
        ...                 tree(6)]),
        ...           tree(2)])
        >>> tree_max(t)
        6
        >>> s = tree(11,
        ...           [tree(32,
        ...                  [tree(4),
        ...                   tree(15,
        ...                         [tree(21)
        ...                          tree(45)]),
        ...                   tree(8)]),
        ...            tree(2,
        ...                 [tree(12),
        ...                  tree(2)])])
        >>> tree_max(s)
        45
        """
        self.assertEqual(tree_max(t), 6)
        self.assertEqual(tree_max(s), 45)

    def test_problems_3_2(self):
        """Return the height of a tree
        >>> t = tree(1,
        ...          [tree(3,
        ...                [tree(4),
        ...                 tree(5),
        ...                 tree(6)]),
        ...           tree(2)])
        >>> height(t)
        2
        >>> s = tree(11,
        ...           [tree(32,
        ...                  [tree(4),
        ...                   tree(15,
        ...                         [tree(21),
        ...                          tree(45)]),
        ...                   tree(8)]),
        ...            tree(2,
        ...                 [tree(12),
        ...                  tree(2)])])
        >>> height(s)
        3
        """
        self.assertEqual(height(t), 2)
        self.assertEqual(height(s), 3)

    def test_problems_3_3(self):
        """Return a tree with the square of every element in 't'. It shouldn't modify the original tree
        >>> t = tree(1,
        ...          [tree(3,
        ...                [tree(4),
        ...                 tree(5),
        ...                 tree(6)]),
        ...           tree(2)])
        >>> print_tree(square_tree(t))
        1
          9
            16
            25
            36
          4
        >>> print_tree(t)
        1
          3
            4
            5
            6
          2
        """
        original_t = t[::]
        self.assertEqual(square_tree(t), squared_t)
        self.assertEqual(t, original_t)

    def test_problems_3_4(self):
        """Return a list showing the branch values for getting to a node labeled 'x'
        >>> t = tree(2,
        ...          [tree(7,
        ...                [tree(3),
        ...                 tree(6,
        ...                      [tree(5),
        ...                       tree(11)])]),
        ...           tree(15)])
        >>> find_path(t, 5)
        [2, 7, 6, 5]
        >>> find_path(t, 10) # returns None
        """
        self.assertEqual(find_path(u, 5), [2, 7, 6, 5])
        self.assertEqual(find_path(u, 10), None)
        self.assertEqual(find_path(u, 6), [2, 7, 6])

    def test_problems_3_5(self):
        """A function that takes in a tree and a depth 'k' and returns a new
        tree that contains only the first 'k' levels of the original tree.
        >>> t = tree(2,
        ...          [tree(7,
        ...                [tree(3),
        ...                 tree(6,
        ...                      [tree(5),
        ...                       tree(11)])]),
        ...           tree(15)])
        >>> print_tree(prune(t, 2))
        2
          7
            3
            6
          15
        >>> print_tree(prune(t, 0))
        2
        """

        expected_prune_2 = test_utils.cleandoc(
            """
            2
              7
                3
                6
              15
            """
        )

        self.assertPrinted(print_tree, [prune(u, 2)], expected_prune_2)
        self.assertPrinted(print_tree, [prune(u, 0)], "2")

if __name__ == "__main__":
    unittest.main()