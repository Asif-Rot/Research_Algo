import doctest
from typing import Callable


class Graph:
    """
    This class is for applying the Strategy pattern by sending an algorithm as an argument.
    We have 2 algorithms:
    1. Dijkstra
        a. This algorithm requires a start vertex.
    2. Floyd-Warshall

    The first graph we will use for the tests will look like that:

             15
       1 <------------- 4
       ^ \          /   ^
      ||    \ 30  /    ||
    5 ||50    \ /    5 || 15
      ||      / \      ||
      ||    / 5   \    ||
      >   /         \  <
      2 -------------> 3
             15

    >>> mat = [[0, 5, float('inf'), float('inf')], [50, 0, 15, 5], [30, float('inf'), 0, 15], [15, float('inf'), 5, 0]]
    >>> g = Graph(mat)
    >>> g.shortest_path(g.dijkstra, 0)
    Distance from vertex 0 to vertex 0 is 0
    Distance from vertex 0 to vertex 1 is 5
    Distance from vertex 0 to vertex 2 is 15
    Distance from vertex 0 to vertex 3 is 10
    >>> g.shortest_path(g.floyd_warshall)
    Distance from vertex 0 to every node in the graph (ordered by nodes): [0, 5, 15, 10]
    Distance from vertex 1 to every node in the graph (ordered by nodes): [20, 0, 10, 5]
    Distance from vertex 2 to every node in the graph (ordered by nodes): [30, 35, 0, 15]
    Distance from vertex 3 to every node in the graph (ordered by nodes): [15, 20, 5, 0]
    >>> g.shortest_path(g.dijkstra, 1)
    Distance from vertex 0 to vertex 0 is 20
    Distance from vertex 0 to vertex 1 is 0
    Distance from vertex 0 to vertex 2 is 10
    Distance from vertex 0 to vertex 3 is 5
    >>> mat2 = [[0,   5,  float('inf'), 10], [float('inf'),  0,  3,  float('inf')], [float('inf'), float('inf'), 0,   1], [float('inf'), float('inf'), float('inf'), 0] ]
    >>> g.shortest_path(g.dijkstra, 0)
    Distance from vertex 0 to vertex 0 is 0
    Distance from vertex 0 to vertex 1 is 5
    Distance from vertex 0 to vertex 2 is 15
    Distance from vertex 0 to vertex 3 is 10
    >>> g.shortest_path(g.floyd_warshall)
    Distance from vertex 0 to every node in the graph (ordered by nodes): [0, 5, 15, 10]
    Distance from vertex 1 to every node in the graph (ordered by nodes): [20, 0, 10, 5]
    Distance from vertex 2 to every node in the graph (ordered by nodes): [30, 35, 0, 15]
    Distance from vertex 3 to every node in the graph (ordered by nodes): [15, 20, 5, 0]
    """
    def __init__(self, g: list):
        self.g = g

    def min_distance(self, distance, queue):
        minimum = float("Inf")
        min_index = -1
        for i in range(len(distance)):
            if distance[i] < minimum and i in queue:
                minimum = distance[i]
                min_index = i
        return min_index

    def dijkstra(self, start_vertex):
        row = len(self.g)
        col = len(self.g[0])
        dist = [float("inf")] * row
        parent = [-1] * row
        dist[start_vertex] = 0
        queue = []

        for i in range(row):
            queue.append(i)

        while queue:
            u = self.min_distance(dist, queue)
            queue.remove(u)

            for i in range(col):
                if self.g[u][i] and i in queue:
                    if dist[u] + self.g[u][i] < dist[i]:
                        dist[i] = dist[u] + self.g[u][i]
                        parent[i] = u
        return dist

    def floyd_warshall(self):
        distance = list(map(lambda i: list(map(lambda j: j, i)), self.g))
        size = len(self.g)

        # Adding vertices individually
        for k in range(size):
            for i in range(size):
                for j in range(size):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        return distance

    def shortest_path(self, algorithm: Callable, *args):
        try:
            arr = algorithm(*args)
            if args != ():
                for v in range(len(arr)):
                    print("Distance from vertex 0 to vertex", v, "is", arr[v])
            else:
                for i in range(len(arr)):
                    print(f'Distance from vertex {i} to every node in the graph (ordered by nodes): {arr[i]}')
        except TypeError:
            print("You need to insert a start vertex for Dijkstra algorithm")


if __name__ == '__main__':
    doctest.testmod()
