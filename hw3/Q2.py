import doctest
import os


def lastcall(func):
    """
    This is a decorator function.
    First we check if there is a file that keeps the last call, if there isn't, we will create one.
    Then, we get in to the inner function and check if there is an output saved in the file, if there is, we print it.
    We save the result from the function in the file.
    Finally, we print the function and return it.

    >>> summarize("hi")
    I already told you that the answer is hi!

    >>> summarize("Asif")
    I already told you that the answer is hi!
    I already told you that the answer is Asif!

    >>> f(2)
    I already told you that the answer is Asif!
    I already told you that the answer is 4!

    """
    if not os.path.exists('last_calls.txt'):
        open('last_calls.txt', 'w').close()

    def inner(*args, **kwargs):

        # retrieve last call output from last_calls.txt file
        with open('last_calls.txt', "r") as f:
            try:
                previous_outputs = f.readlines()[-1].rstrip()
            except:
                previous_outputs = []

        if previous_outputs:
            # for item in previous_outputs:
            print(f'I already told you that the answer is {previous_outputs}!')

        # append the output in the historic outputs txt file
        with open('last_calls.txt', 'a') as ff:
            ff.write(str(func(*args, **kwargs)) + "\n")

        print(f'I already told you that the answer is {func(*args, **kwargs)}!')
        print()

        return func(*args, **kwargs)

    return inner


@lastcall
def summarize(*args):
    result = ""
    for i in args:
        result += i
    return result


@lastcall
def f(x: int):
    return x ** 2

@lastcall
def f_float(x: float):
    return x + 1


if __name__ == '__main__':
    doctest.testmod()

    summarize("hello")  # Should print "I already told you that the answer is hello!"
    summarize("my name is")  # Should print "I already told you that the answer is hello!\nI already told you that the
    # answer is my name is!"
    summarize("Asif")  # Should print "I already told you that the answer is my name is!\nI already told you that the
    # answer is Asif!"
    f(2)  # Should print "I already told you that the answer is Asif!\nI already told you that the
    # answer is 4!"
    f(10)  # Should print "I already told you that the answer is 4!\nI already told you that the
    # answer is 100!"
    f_float(2.5) # Should print "I already told you that the answer is 100!\nI already told you that the
    # answer is 3.5!"
