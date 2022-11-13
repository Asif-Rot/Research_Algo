import os


def lastcall(func):
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


if __name__ == '__main__':
    summarize("hello")
    summarize("my name is")
    summarize("Asif")
    f(2)
    f(10)
