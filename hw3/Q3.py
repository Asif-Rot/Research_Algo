class List(list):
    def __getitem__(self, arg):
        if isinstance(arg, int):
            return super().__getitem__(arg)
        if len(arg) == 1:
            return super().__getitem__(arg[0])
        return List(super().__getitem__(arg[0]))[arg[1:]]


if __name__ == '__main__':
    mylist = List([
        [[1, 2, 3, 33], [4, 5, 6, 66]],
        [[7, 8, 9, 99], [10, 11, 12, 122]],
        [[13, 14, 15, 155], [16, 17, 18, 188]],
    ]
    )
    print(mylist[0, 1, 3])
