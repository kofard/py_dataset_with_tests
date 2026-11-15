def is_safe(node: int, color: int, graph: list[list[int]], num_vertices: int, col: list[int]) -> bool:
    """Check if it is safe to assign a color to a node."""
    return all((not (graph[node][k] == 1 and col[k] == color) for k in range(num_vertices)))

def solve(node: int, col: list[int], max_colors: int, num_vertices: int, graph: list[list[int]]) -> bool:
    """Recursively try to color the graph using at most max_colors."""
    if node == num_vertices:
        return True
    for c in range(1, max_colors + 1):
        if is_safe(node, c, graph, num_vertices, col):
            col[node] = c
            if solve(node + 1, col, max_colors, num_vertices, graph):
                return True
            col[node] = 0
    return False

def graph_coloring(graph: list[list[int]], max_colors: int, num_vertices: int) -> bool:
    """Determine if the graph can be colored with at most max_colors."""
    col = [0] * num_vertices
    return solve(0, col, max_colors, num_vertices, graph)