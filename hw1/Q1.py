import doctest


def f(x: int, y: float, z):
    return x + y + z


def f2(x: str, y: str, z: str, t):
    return x + y + z + t


def safe_call(func, **kwargs):  # ** For number of args
    """
        >>> safe_call(f, x=5, y=7.0, z=3)
        15.0
        >>> safe_call(f, x=5.0, y="abc", z=3)
        Traceback (most recent call last):
        ...
        TypeError: One or more of the arguments is not correct
        >>> safe_call(f2, x="this ", y="is ", z="gr", t="8")
        'this is gr8'
        >>> safe_call(f2, x="this ", y="is ", z="gr", t=8)
        Traceback (most recent call last):
        ...
        TypeError: can only concatenate str (not "int") to str
        >>> safe_call(f, y=7, z=0.5)
        Traceback (most recent call last):
        ...
        TypeError: One or more of the arguments is not correct
    """
    annotations = func.__annotations__
    # Calling some function
    for key in kwargs:
        if key in annotations and not isinstance(kwargs[key], annotations[key]):
            raise TypeError(
                "One or more of the arguments is not correct")  # In case one of the arguments is not in the right type
    return func(**kwargs)


if __name__ == '__main__':
    doctest.testmod()

    print("first check (OK): ", safe_call(f, x=5, y=7.0, z=3))
    print("second check (ERROR)", safe_call(f, x=2.0, y="abc", z=0.5))
    print("third check with different function (OK)", safe_call(f2, x="this ", y="is ", z="gr", t="8"))
    print("forth check with different function (ERROR)",
          safe_call(f2, x="this ", y="is ", z="gr", t=8))  # Error - can't do str+int
    print("fifth check (ERROR)", safe_call(f, y=7, z=0.5))  # Error - missing one argument

