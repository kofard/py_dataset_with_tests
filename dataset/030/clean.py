from __future__ import annotations

def print_distance(distance: list[float], src) -> None:
    print(f'Vertex\tShortest Distance from vertex {src}')
    for i, d in enumerate(distance):
        print(f'{i}\t\t{d}')

def check_negative_cycle(graph: list[dict[str, int]], distance: list[float], edge_count: int) -> bool:
    for j in range(edge_count):
        u, v, w = (graph[j][k] for k in ['src', 'dst', 'weight'])
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            return True
    return False

def bellman_ford(graph: list[dict[str, int]], vertex_count: int, edge_count: int, src: int) -> list[float]:
    """Returns shortest paths from a vertex src to all
    other vertices."""
    distance = [float('inf')] * vertex_count
    distance[src] = 0.0
    for _ in range(vertex_count - 1):
        for j in range(edge_count):
            u, v, w = (graph[j][k] for k in ['src', 'dst', 'weight'])
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
    negative_cycle_exists = check_negative_cycle(graph, distance, edge_count)
    if negative_cycle_exists:
        raise Exception('Negative cycle found')
    return distance