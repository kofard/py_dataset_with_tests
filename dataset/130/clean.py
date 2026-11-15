from collections import deque

def topological_sort(graph: dict[int, list[int]]) -> list[int] | None:
    """Perform topological sorting of a Directed Acyclic Graph (DAG)
    using Kahn's Algorithm via Breadth-First Search (BFS).

    Topological sorting is a linear ordering of vertices in a graph such that for
    every directed edge u → v, vertex u comes before vertex v in the ordering.

    Parameters:
    graph: Adjacency list representing the directed graph where keys are
           vertices, and values are lists of adjacent vertices.

    Returns:
    The topologically sorted order of vertices if the graph is a DAG.
    Returns None if the graph contains a cycle.

    Example:"""
    indegree = dict.fromkeys(graph, 0)
    queue: deque[int] = deque()
    topo_order = []
    processed_vertices_count = 0
    for values in graph.values():
        for i in values:
            indegree[i] += 1
    for vertex, count in indegree.items():
        if count == 0:
            queue.append(vertex)
    while queue:
        vertex = queue.popleft()
        processed_vertices_count += 1
        topo_order.append(vertex)
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if processed_vertices_count != len(graph):
        return None
    return topo_order