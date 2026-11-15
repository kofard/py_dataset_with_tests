"""Breadth-first search the shortest path implementations.
doctest:
python -m doctest -v breadth_first_search_shortest_path_2.py
Manual test:
python breadth_first_search_shortest_path_2.py
"""
from collections import deque
demo_graph = {'A': ['B', 'C', 'E'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F', 'G'], 'D': ['B'], 'E': ['A', 'B', 'D'], 'F': ['C'], 'G': ['C']}

def bfs_shortest_path(graph: dict, start, goal) -> list[str]:
    """Find the shortest path between `start` and `goal` nodes.
    Args:
        graph (dict): node/list of neighboring nodes key/value pairs.
        start: start node.
        goal: target node.
    Returns:
        Shortest path between `start` and `goal` nodes as a string of nodes.
        'Not found' string if no path found.
    Example:"""
    explored = set()
    queue = deque([[start]])
    if start == goal:
        return [start]
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.add(node)
    return []

def bfs_shortest_path_distance(graph: dict, start, target) -> int:
    """Find the shortest path distance between `start` and `target` nodes.
    Args:
        graph: node/list of neighboring nodes key/value pairs.
        start: node to start search from.
        target: node to search for.
    Returns:
        Number of edges in the shortest path between `start` and `target` nodes.
        -1 if no path exists.
    Example:"""
    if not graph or start not in graph or target not in graph:
        return -1
    if start == target:
        return 0
    queue = deque([start])
    visited = set(start)
    dist = {start: 0, target: -1}
    while queue:
        node = queue.popleft()
        if node == target:
            dist[target] = dist[node] if dist[target] == -1 else min(dist[target], dist[node])
        for adjacent in graph[node]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append(adjacent)
                dist[adjacent] = dist[node] + 1
    return dist[target]