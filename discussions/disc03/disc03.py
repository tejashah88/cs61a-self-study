def tree_max(t):
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
    ...                         [tree(21),
    ...                          tree(45)]),
    ...                   tree(8)]),
    ...            tree(2,
    ...                 [tree(12),
    ...                  tree(2)])])
    >>> tree_max(s)
    45
    """
    """BEGIN PROBLEM 3.1"""
    # strat: simply collect all the labels recursively and get the max value from the branches and leaves
    return max([label(t)] + [tree_max(b) for b in branches(t)])
    """END PROBLEM 3.1"""

def height(t):
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
    """BEGIN PROBLEM 3.2"""
    # strat:
    #  - recursively walk the branches and keep track of each depth and we go in one layer at a time
    #  - for each branch, take the max value after calling height() for each branch and add 1 before returning it
    #  - if we hit a leaf, then there's no more branches to go through...just return 0
    return 0 if is_leaf(t) else (1 + max([height(b) for b in branches(t)]))
    """END PROBLEM 3.2"""

def square_tree(t):
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
    """BEGIN PROBLEM 3.3"""
    # no need to make an explicit copy (via splicing) of the tree when you can reconstruct one from the constructor directly
    return tree(label(t) ** 2, [square_tree(b) for b in branches(t)])
    """END PROBLEM 3.3"""


def find_path(tree, x):
    """Return a list showing the branch values for getting to a node labeled 'x'.
       Extra challenge (for me): if x is detected in tree while parsing branches, return the path immediately
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
    >>> find_path(t, 6)
    [2, 7, 6]
    """
    """BEGIN PROBLEM 3.4"""
    # strat:
    #  - walk through the branches until we find the leaves or we find a label that matches 'x'
    #  - if 'x' exists in the original tree, then return it inside an array and add the connecting branches along the way
    #  - otherwise, return None if 'x' doesn't exist in the tree
    if label(tree) == x:
        return [x] # we found 'x', return it inside an array
    for path in [find_path(branch, x) for branch in branches(tree)]:
        if path: # if this is a truthy value, then attach the branch's label in front of the path value and return it
            return [label(tree)] + path
    """END PROBLEM 3.4"""

def prune(t, k):
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
    """
    """BEGIN PROBLEM 3.5"""
    if k == 0:
        return tree(label(t))
    return tree(label(t), [prune(b, k - 1) for b in branches(t)])
    """END PROBLEM 3.5"""

# Tree-related functions

# Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

# Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

# For convenience
def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root."""
    print('  ' * indent + str(label(t)))
    [print_tree(branch, indent + 1) for branch in branches(t)]

if __name__ == "__main__":
    import doctest
    doctest.testmod(exclude_empty=True)