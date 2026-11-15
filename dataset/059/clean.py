from collections import defaultdict, deque

def is_bipartite_dfs(graph: dict[int, list[int]]) -> bool:
    """Check if a graph is bipartite using depth-first search (DFS).

    Args:
        `graph`: Adjacency list representing the graph.

    Returns:
        ``True`` if bipartite, ``False`` otherwise.

    Checks if the graph can be divided into two sets of vertices, such that no two
    vertices within the same set are connected by an edge.

    Examples:"""

    def depth_first_search(node: int, color: int) -> bool:
        """
        Perform Depth-First Search (DFS) on the graph starting from a node.

        Args:
            node: The current node being visited.
            color: The color assigned to the current node.

        Returns:
            True if the graph is bipartite starting from the current node,
            False otherwise.
        """
        if visited[node] == -1:
            visited[node] = color
            if node not in graph:
                return True
            for neighbor in graph[node]:
                if not depth_first_search(neighbor, 1 - color):
                    return False
        return visited[node] == color
    visited: defaultdict[int, int] = defaultdict(lambda: -1)
    for node in graph:
        if visited[node] == -1 and (not depth_first_search(node, 0)):
            return False
    return True

def is_bipartite_bfs(graph: dict[int, list[int]]) -> bool:
    """Check if a graph is bipartite using a breadth-first search (BFS).

    Args:
        `graph`: Adjacency list representing the graph.

    Returns:
        ``True`` if bipartite, ``False`` otherwise.

    Check if the graph can be divided into two sets of vertices, such that no two
    vertices within the same set are connected by an edge.

    Examples:"""
    visited: defaultdict[int, int] = defaultdict(lambda: -1)
    for node in graph:
        if visited[node] == -1:
            queue: deque[int] = deque()
            queue.append(node)
            visited[node] = 0
            while queue:
                curr_node = queue.popleft()
                if curr_node not in graph:
                    continue
                for neighbor in graph[curr_node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1 - visited[curr_node]
                        queue.append(neighbor)
                    elif visited[neighbor] == visited[curr_node]:
                        return False
    return True