import numpy as np
import cvxpy as cp
import time
import matplotlib.pyplot as plt


def linear_equation_compare(start, end, x):
    """
    In this function we are going to compare between two packages (Numpy & Cvxpy) and check who wins in terms of time.

    :param start: The start index for the numpy randint function
    :param end: The end index for the numpy randint function
    :param x: The matrix

    :return: Times that took to solve the liner equations for each package
    """

    # Creating random Numpy arrays
    lhs = np.random.randint(start, end, (x, x))
    rhs = np.random.randint(start, end, x)

    # Solving the liner equation with Numpy + Checking times
    time_ans_np_start = time.time()
    np.linalg.solve(lhs, rhs)
    time_ans_np_end = time.time()

    # Creating Linear equation with Cvxpy
    cp_var = cp.Variable(x)
    constraints = [lhs @ cp_var == rhs]
    obj = cp.Minimize(cp.sum(lhs @ cp_var - rhs))
    prob = cp.Problem(obj, constraints)

    # Solving the liner equation with Cvxpy + Checking times
    time_ans_cp_start = time.time()
    prob.solve()
    time_ans_cp_end = time.time()

    # Times
    time_np = time_ans_np_end - time_ans_np_start
    time_cp = time_ans_cp_end - time_ans_cp_start

    return time_np, time_cp


def plot_graph(start, end, i):
    """
    This function will draw the graph of times from the linear_equation_compare function.

    :param start: The start index for the numpy randint function
    :param end: The end index for the numpy randint function
    :param i: The matrix
    """
    times_np = {}
    times_cp = {}

    for j in range(1, i):
        x = linear_equation_compare(start, end, j)
        times_np[j] = x[0]
        times_cp[j] = x[1]

    plt.title("Compare times between cp & np results")
    plt.plot(times_np.keys(), times_np.values(), color="green")
    plt.plot(times_cp.keys(), times_cp.values(), color="blue")
    plt.legend(['Numpy', 'Cvxpy'])
    plt.show()


if __name__ == '__main__':
    plot_graph(1, 100, 50)
