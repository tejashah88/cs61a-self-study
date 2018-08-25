""" Optional Questions for Lab 07 """

from lab07 import *

# Q6
def remove_all(link, value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    # Link(1, Link(2, Link(3)))
    # Link(1, Link(3))

    # empty tuples will throw an error
    if not link or not link.rest:
        return

    if link.second == value:
        link.rest = link.rest.rest
        # make sure to not skip over elements when removing
        remove_all(link, value)
    else:
        # keep on going
        remove_all(link.rest, value)

# Q7
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """

    if not link:
        return

    if isinstance(link.first, Link):
        deep_map_mut(fn, link.first)
    else:
        link.first = fn(link.first)
    deep_map_mut(fn, link.rest)

# Q8
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    # linear space, theta(n)
    storage = []
    while link.rest:
        if link not in storage:
            storage.append(link)
            link = link.rest
        else:
            return True
    return False

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """

    """
    Approach: have a slow and fast track: slow one consumes the 'rest' of the linked
    list once while the fast one consumes the 'rest' of the list twice. The idea is to
    find out if either of them hit a dead end (implying no cycle) or they equal each
    other (implying a cycle).
    """

    # constant space, theta(1)
    lazy_trak, sanic_trak = link, link.rest
    # if this becomes false, we found a dead end while consuming 'rest'
    while sanic_trak is not Link.empty:
        if sanic_trak.rest is Link.empty:
            # dead end detected => no cycle found
            return False
        elif lazy_trak == sanic_trak or sanic_trak.rest == lazy_trak:
            # match found => cycle detected
            return True
        else:
            # keep on racing
            lazy_trak, sanic_trak = lazy_trak.rest, sanic_trak.rest.rest
    return False

# Q9
def reverse_other(t):
    """Mutates the tree such that nodes on every other (even_indexed) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    # Basically, given a tree 't', when the depth level is even (including 0),
    # reverse the labels of the branches of that level (i.e odd levels will be altered)
    def helper(t, depth=0):
        if depth % 2 == 0:
            # switcharoo le labels
            labels = [b.label for b in t.branches]
            for b in t.branches:
                # popping removes the last element of a list, hence giving the reverse effect
                # since we got the labels in the same order as we iterated through the branches
                b.label = labels.pop()
        for b in t.branches:
            # into the depths of recursion hell
            helper(b, depth + 1)
    helper(t)
