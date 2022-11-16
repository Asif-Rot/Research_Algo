import doctest


def neighbor_function(node):
    """
    This function gets all the given nodes' neighbors in horizontal and vertical order.
    :return: list of nodes
    """
    (x, y) = node

    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def bfs(start, end, neighbor_func):
    """
    BFS - Breadth First Search
    Finding the path from a starting node to a specific node.

    :param start: start node (x, y)
    :param end: end node  (x, y)
    :param neighbor_func: function that gives all the neighbors
    :return: the path from the start node to the end node with the node's neighbors

    >>> bfs((0, 0), (0, 0), neighbor_function)
        [(0, 0)]
    >>> bfs((0, 0), (4, 3), neighbor_function)
        [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3)]
    >>> bfs((0, 1), (0, 0), neighbor_function)
        [(0, 1), (0, 0)]
    >>> bfs((3, 2), (0, 0), neighbor_function)
        [(3, 2), (2, 2), (1, 2), (0, 2), (0, 1), (0, 0)]
    >>> bfs((5, 2), (-1, -1), neighbor_function)
        [(5, 2), (4, 2), (3, 2), (2, 2), (1, 2), (0, 2), (-1, 2), (-1, 1), (-1, 0), (-1, -1)]
    """

    # init a queue of paths with the start node
    queue = [[start]]
    visited = [start]

    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path

        for nei in neighbor_func(node):
            if nei not in visited:
                visited.append(nei)
                new_path = list(path)
                new_path.append(nei)
                queue.append(new_path)


if __name__ == '__main__':
    doctest.testmod()
    print(bfs((0, 0), (0, 0), neighbor_function))  # Start and end are the same
    print(bfs((0, 0), (4, 3), neighbor_function))  # Long way
    print(bfs((0, 1), (0, 0), neighbor_function))  # One step
    print(bfs((3, 2), (0, 0), neighbor_function))  # Going back
    print(bfs((5, 2), (-1, -1), neighbor_function))  # Checking negative numbers
    print(bfs((0, 0), (4, 4), neighbor_function))  # Checking same x, y
