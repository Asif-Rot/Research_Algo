import doctest


class List(list):
    def __getitem__(self, arg):
        """
        This function gets the item from any structure of a list.
        We check if we got only one number, if so, we will return the value of the argument in this position.
        We check if its length equals 1, if so, we will return the first argument / list.
        We search the argument from the start of the list to the end and return it.

        >>> myList2 = List([1, 2])
        >>> mylist2[0]
        1
        >>> myList5 = List([ [['a', 'b', 'c'], [2, 5, 8]], [[1, 9]]])
        >>> myList5[1, 0, 1]
        9
        """
        if isinstance(arg, int):
            return super().__getitem__(arg)
        if len(arg) == 1:
            return super().__getitem__(arg[0])
        return List(super().__getitem__(arg[0]))[arg[1:]]


if __name__ == '__main__':
    doctest.testmod()

    mylist = List([
        [[1, 2, 3, 33], [4, 5, 6, 66]],
        [[7, 8, 9, 99], [10, 11, 12, 122]],
        [[13, 14, 15, 155], [16, 17, 18, 188]],
    ]
    )

    myList2 = List([1, 2])
    myList3 = List([[1, 2], [3, 4]])
    myList4 = List([[1, 2, 3], [4, 5], [6, 7, 8, 9]])
    myList5 = List([
        [['a', 'b', 'c'], [2, 5, 8]],
        [[1, 9]]
    ])

    print(mylist[0, 1, 3])  # Should print 66
    print(myList2[0])  # Should print 1
    print(myList3[0, 1])  # Should print 2
    print(myList4[2, 1])  # Should print 7
    print(myList5[1, 0, 1])  # Should print 9
    print(myList5[1])  # Should print [[1, 9]]
