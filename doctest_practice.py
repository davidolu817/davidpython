import doctest

import practice


def add(a, b):
    """
    >>> add(3, 5)
    8
    """
    return a + b


if __name__ == '__main__':
    doctest.testmod()