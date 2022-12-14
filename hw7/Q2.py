import networkx as nx
import math
import matplotlib.pyplot as plt
import numpy as np
import random


# Find the O(|V |/(log|V |)) apx of independent set in the worst case
def apx_of_independent_set(v):
    return v / (math.pow(math.log(v, 2), 2))


def apx_max_independent_set(g):
    """
    This function will calculate:
        - The maximal independent set in a random graph (G[n,p])
        - The approximation of maximum independent set in a random graph (G[n,p])
        - The approximation theory of independent set with the length of a random graph (G[n,p])
    :return: The comparison between the apx and the exact algo + The result of the apx theory
    """
    max_algo = nx.maximal_independent_set(g)
    apx_algo = nx.approximation.maximum_independent_set(g)
    apx_theory = apx_of_independent_set(len(g))

    return abs(len(apx_algo) - len(max_algo)), round(apx_theory, 2)


def plot_graph(n):
    """
    This function will plot a graph from all the calculations
    """
    labels = []
    algo = []
    theory = []
    for j in range(1, n):
        p = round(random.random(), 1)
        g = nx.gnp_random_graph((j*10), p)
        labels.append(((j*10), p))
        result = apx_max_independent_set(g)
        algo.append(result[0])
        theory.append(result[1])

    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, algo, width, label='apx')
    rects2 = ax.bar(x + width / 2, theory, width, label='theory')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('ratio')
    ax.set_title('Compare between apx and theory')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()


if __name__ == '__main__':
    plot_graph(50)

