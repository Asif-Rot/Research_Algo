import doctest


def print_sorted(x):
    """
    printing the sorted object with an inner helper function.
    :param x: The object we need to sort
    """

    def helper(y):
        """
        The helper function checks if the object contains a single character, list, dictionary, tuple or list.
        If it has one of the above, it will sort it and will return the object sorted at the end.
        :param y: the parameter we get from the function
        :return: sorted object

        >>> helper([3, 2, 1, 4])
        [1, 2, 3, 4]
        >>> helper({"one": 1, "two": "2", 3: {1, 3, 2}})
        {'one': 1, 'two': '2', 3: [1, 2, 3]}
        >>> helper((5, 4, 7, 9, 1))
        (1, 4, 5, 7, 9)
        >>> helper({4, 2, 1, 6})
        [1, 2, 4, 6]
        >>> helper({"a": 1, "b": {3, 2, 5}, 1: {5, 5, 1}, "c": (2, 1), 6: 6})
        {'a': 1, 'b': [2, 3, 5], 'c': (1, 2), 1: [1, 5], 6: 6}
        >>> helper("hi")
        hi
        """

        if isinstance(y, list):
            sorted_list = []
            after_sort = sorted(y, key=lambda t: str(t))
            for lst in after_sort:
                sorted_list.append(helper(lst))
            return sorted_list

        elif isinstance(y, dict):
            sorted_dict = {}
            data = dict(sorted(y.items(), key=lambda t: str(t)))
            for key, value in data.items():
                sorted_dict[key] = helper(value)
            return sorted_dict

        elif isinstance(y, tuple):
            sorted_tuple = []
            after_sort = sorted(y, key=lambda t: str(t))
            for tup in after_sort:
                sorted_tuple.append(helper(tup))
            return tuple(sorted_tuple)

        elif isinstance(y, set):
            sorted_set = []
            after_sort = sorted(y, key=lambda t: str(t))
            for s in after_sort:
                sorted_set.append(helper(s))
            return sorted_set

        else:
            return y

    print(helper(x))


if __name__ == '__main__':
    doctest.testmod()

    print_sorted([3, 2, 1, 4])  # list
    print_sorted({"one": 1, "two": "2", 3: {1, 3, 2}})  # dict
    print_sorted((5, 4, 7, 9, 1))  # tuple
    print_sorted({4, 2, 1, 6})  # set
    print_sorted({"a": 1, "b": {3, 2, 5}, 1: {5, 5, 1}, "c": (2, 1), 6: 6})  # combined
    print_sorted("hi")  # str
