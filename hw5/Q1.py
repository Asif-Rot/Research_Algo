import doctest
from itertools import chain, combinations


class bounded_subsets:
    """
    This class is created in order to define an iterator that yields all subsets of some set.
    All the subsets should be the sum (or less than the sum) of some positive integer.

    >>> res = []
    >>> for subset in bounded_subsets([1, 2, 3], 4): res.append(subset)
    >>> print(res)
    [[], [1], [2], [3], [1, 2], [1, 3]]
    >>> for t in zip(range(5), bounded_subsets(range(1, 100), 1000000000000)): print(t)
    (0, [])
    (1, [1])
    (2, [2])
    (3, [3])
    (4, [4])
    >>> res2 = []
    >>> for subset in bounded_subsets([1], 1): res2.append(subset)
    >>> print(res2)
    [[], [1]]
    >>> res3 = []
    >>> for subset in bounded_subsets([], 1): res3.append(subset)
    >>> print(res3)
    [[]]
    >>> res4 = []
    >>> for subset in bounded_subsets([1, -2], 2): res4.append(subset)
    Traceback (most recent call last):
    ...
    TypeError: All arguments in the list should be positive integers
    >>> res5 = []
    >>> for subset in bounded_subsets([1, 2], -2): res5.append(subset)
    Traceback (most recent call last):
    ...
    TypeError: second attribute should be a positive integer
    >>> res6 = []
    >>> for subset in bounded_subsets(["test", "test2"], 2): res6.append(subset)
    Traceback (most recent call last):
    ...
    TypeError: All arguments in the list should be positive integers
    >>> res7 = []
    >>> for subset in bounded_subsets([1, 2, 3, 4], 10): res7.append(subset)
    >>> print(res7)
    [[], [1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]

    """
    def __init__(self, s: list, c: int):
        self.s = self._is_valid_s(sorted(s))  # Checking if the list is valid and sort it if it is
        self.c = self._is_valid_c(c)  # Checking if the integer is valid.

    def __iter__(self):
        subsets = chain.from_iterable(combinations(self.s, r) for r in range(len(self.s) + 1))
        for subset in subsets:
            if sum(subset) <= self.c:
                yield list(subset)

    def _is_valid_s(self, lst):
        if not (isinstance(lst, list)):  # Check if the type is list
            raise TypeError("first attribute should be a list")
        for arg in lst:
            if not isinstance(arg, int) or arg < 1:  # Check for every argument if it is a positive integer
                raise TypeError("All arguments in the list should be positive integers")
        return lst

    def _is_valid_c(self, c):
        if not isinstance(c, int):  # Check if the type is integer
            raise TypeError("second attribute should be an integer")
        if c < 1:  # Check if it is a positive integer
            raise TypeError("second attribute should be a positive integer")
        return c


if __name__ == '__main__':
    doctest.testmod()
