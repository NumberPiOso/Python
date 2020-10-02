"""
This is pure Python implementation of fibonacci search.

Resources used:
https://en.wikipedia.org/wiki/Fibonacci_search_technique

For doctests run following command:
python3 -m doctest -v fibonacci_search.py

For manual testing run:
python3 fibonacci_search.py
"""
from __future__ import annotations
from functools import lru_cache
import sys


@lru_cache()
def fibonacci(k: int) -> int:
    """Finds fibonacci number in index k.

    Parameters
    ----------
    k : int
        Index of fibonacci.

    Returns
    -------
    int
        Fibonacci number in position k.

    >>> print(fibonacci(0))
    0
    >>> print(fibonacci(2))
    1
    >>> print(fibonacci(5))
    5
    >>> print(fibonacci(15))
    610
    """
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return fibonacci(k - 1) + fibonacci(k - 2)


def fibonacci_search(arr: List[int], val: int) -> int:
    """A pure Python implementation of a fibonacci search algorithm.

    Parameters
    ----------
    arr : List[int]
        List of sorted elements.
    val : int
        Element to search in list.

    Returns
    -------
    int
        The index of the element in the array.
        -1 if the element is not found.

    >>> print(fibonacci_search([4, 5, 6, 7], 4))
    0
    >>> print(fibonacci_search([4, 5, 6, 7], -10))
    -1
    >>> print(fibonacci_search([-18, 2], -18))
    0
    >>> print(fibonacci_search([5], 5))
    0
    >>> print(fibonacci_search(['a', 'c', 'd'], 'c'))
    1
    >>> print(fibonacci_search(['a', 'c', 'd'], 'f'))
    -1
    >>> print(fibonacci_search([], 1))
    -1
    >>> print(fibonacci_search([.1, .4 , 7], .4))
    1
    >>> fibonacci_search([], 9)
    -1
    """
    n = len(arr)
    # Find m such that F_m >= n where F_i is the i_th fibonacci number.
    m = next(x for x in range(sys.maxsize ** 10) if fibonacci(x) >= n)
    k = m
    offset = 0
    while k != 0:
        if arr[offset + fibonacci(k - 1)] == val:
            return fibonacci(k - 1)
        elif val < arr[offset + fibonacci(k - 1)]:
            k = k - 1
        elif val > arr[offset + fibonacci(k - 1)]:
            offset += fibonacci(k - 2)
            k = k - 2
    else:
        return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
