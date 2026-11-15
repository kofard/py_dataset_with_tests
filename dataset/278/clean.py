"""Travelling Salesman Problem (TSP)"""
import itertools
import math

class InvalidGraphError(ValueError):
    """Custom error for invalid graph inputs."""

def euclidean_distance(point1: list[float], point2: list[float]) -> float:
    """Calculate the Euclidean distance between two points in 2D space.

    :param point1: Coordinates of the first point [x, y]
    :param point2: Coordinates of the second point [x, y]
    :return: The Euclidean distance between the two points"""
    try:
        return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
    except TypeError:
        raise ValueError('Invalid input: Points must be numerical coordinates')

def validate_graph(graph_points: dict[str, list[float]]) -> None:
    """Validate the input graph to ensure it has valid nodes and coordinates.

    :param graph_points: A dictionary where the keys are node names,
                         and values are 2D coordinates as [x, y]
    :raises InvalidGraphError: If the graph points are not valid"""
    if not isinstance(graph_points, dict):
        raise InvalidGraphError('Graph must be a dictionary with node names and coordinates')
    for node, coordinates in graph_points.items():
        if not isinstance(node, str) or not isinstance(coordinates, list) or len(coordinates) != 2 or (not all((isinstance(c, (int, float)) for c in coordinates))):
            raise InvalidGraphError('Each node must have a valid 2D coordinate [x, y]')

def travelling_salesman_brute_force(graph_points: dict[str, list[float]]) -> tuple[list[str], float]:
    """Solve the Travelling Salesman Problem using brute force.

    :param graph_points: A dictionary of nodes and their coordinates {node: [x, y]}
    :return: The shortest path and its total distance"""
    validate_graph(graph_points)
    nodes = list(graph_points.keys())
    if len(nodes) < 2:
        raise InvalidGraphError('Graph must have at least two nodes')
    min_path = []
    min_distance = float('inf')
    start_node = nodes[0]
    other_nodes = nodes[1:]
    for perm in itertools.permutations(other_nodes):
        path = [start_node, *perm, start_node]
        total_distance = sum((euclidean_distance(graph_points[path[i]], graph_points[path[i + 1]]) for i in range(len(path) - 1)))
        if total_distance < min_distance:
            min_distance = total_distance
            min_path = path
    return (min_path, min_distance)

def travelling_salesman_dynamic_programming(graph_points: dict[str, list[float]]) -> tuple[list[str], float]:
    """Solve the Travelling Salesman Problem using dynamic programming.

    :param graph_points: A dictionary of nodes and their coordinates {node: [x, y]}
    :return: The shortest path and its total distance"""
    validate_graph(graph_points)
    n = len(graph_points)
    if n < 2:
        raise InvalidGraphError('Graph must have at least two nodes')
    nodes = list(graph_points.keys())
    dist = [[euclidean_distance(graph_points[nodes[i]], graph_points[nodes[j]]) for j in range(n)] for i in range(n)]
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0
    for mask in range(1 << n):
        for u in range(n):
            if mask & 1 << u:
                for v in range(n):
                    if mask & 1 << v == 0:
                        next_mask = mask | 1 << v
                        dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + dist[u][v])
    final_mask = (1 << n) - 1
    min_cost = float('inf')
    end_node = -1
    for u in range(1, n):
        if min_cost > dp[final_mask][u] + dist[u][0]:
            min_cost = dp[final_mask][u] + dist[u][0]
            end_node = u
    path = []
    mask = final_mask
    while end_node != 0:
        path.append(nodes[end_node])
        for u in range(n):
            if mask & 1 << u and dp[mask][end_node] == dp[mask ^ 1 << end_node][u] + dist[u][end_node]:
                mask ^= 1 << end_node
                end_node = u
                break
    path.append(nodes[0])
    path.reverse()
    path.append(nodes[0])
    return (path, min_cost)