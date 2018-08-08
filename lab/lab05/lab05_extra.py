""" Optional questions for Lab 05 """

from lab05 import *

# Shakespeare and Dictionaries
def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = []
        table[prev] += [word]
        prev = word
    return table

def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.

    >>> table = {'Wow': ['!'], 'Sentences': ['are'], 'are': ['cool'], 'cool': ['.']}
    >>> construct_sent('Wow', table)
    'Wow!'
    >>> construct_sent('Sentences', table)
    'Sentences are cool.'
    """
    import random
    result = ''
    while word not in ['.', '!', '?']:
        result += word + ' '
        word = random.choice(table[word.strip()])
    return result.strip() + word

def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

# Uncomment the following two lines
tokens = shakespeare_tokens()
table = build_successors_table(tokens)

def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)

# Q8
def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label
    that appears in vals removed.  Return None if the entire tree is
    pruned away.

    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """

    dup_tree = copy_tree(t)
    should_prune = lambda thing: is_leaf(thing) and label(thing) in vals

    if should_prune(dup_tree):
        return None

    for branch in branches(dup_tree):
        # get the index, we'll pop it if the value is to be pruned
        index = dup_tree.index(branch)
        if is_tree(branch):
            dup_tree[index] = prune_leaves(branch, vals)
            if dup_tree[index] is None: # the value is to be pruned, remove it
                dup_tree.pop(index)
        elif should_prune(branch):
            branch.pop(index)
    return dup_tree

# Q9
def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    dup_tree = copy_tree(t)
    for branch in branches(dup_tree):
        # get the index, we'll append the leaves if we find a leaf
        index = dup_tree.index(branch)
        if is_leaf(branch):
            # append new leaves to the branch
            dup_tree[index] += [tree(val) for val in vals]
        elif is_tree(branch):
            dup_tree[index] = sprout_leaves(branch, vals)
    return dup_tree

# Q10
def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """

    """
    strat:
    1. fill missing spots with zeros
    2. add them up
    """

    # don't modify the trees directly!
    t1, t2 = copy_tree(t1), copy_tree(t2)

    # a function for padding the missing spots to avoid 'not found' errors when 'add'-merging
    def pad_tree(t1, t2):
        while len(branches(t1)) < len(branches(t2)):
            t1.append(tree(0))
        while len(branches(t1)) > len(branches(t2)):
            t2.append(tree(0))
        return t1, t2

    t1, t2 = pad_tree(t1, t2)

    # always add the root labels of the trees
    t1[0] += t2[0]
    for b1, b2 in zip(branches(t1), branches(t2)):
        # just in case we find any missing spots in the branches (might be redundant)
        b1, b2 = pad_tree(b1, b2)
        index_b1 = t1.index(b1)

        if is_leaf(b1) and is_leaf(b2):
            # add the leaves and merge into t1
            b1[0] += b2[0]
            t1[index_b1] = b1
        else:
            # dive into the branches
            t1[index_b1] = add_trees(b1, b2)
    return t1
