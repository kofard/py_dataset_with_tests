"""
Mean Shift Clustering

A non-parametric, centroid-based clustering algorithm that does not require
specifying the number of clusters in advance. It works by iteratively shifting
each data point toward the mean of points within a given bandwidth (radius),
until convergence.

How it works:
    1. Each point starts as its own candidate centroid.
    2. For each candidate, compute the mean of all points within `bandwidth`
       distance (the "window").
    3. Shift the candidate to that mean.
    4. Repeat until candidates stop moving (convergence).
    5. Merge candidates that are closer than `bandwidth` to each other.
    6. Assign each original point to its nearest final centroid.

Key Properties:
    - No need to specify number of clusters (unlike K-Means)
    - Can find arbitrarily shaped clusters (like DBSCAN)
    - Sensitive to the `bandwidth` parameter
    - Deterministic (no random initialization)

Time Complexity:  O(n² * iterations) with brute-force window search
Space Complexity: O(n)

References:
    - https://en.wikipedia.org/wiki/Mean_shift
    - Comaniciu, D. & Meer, P. "Mean Shift: A Robust Approach Toward
      Feature Space Analysis." IEEE TPAMI, 2002.
      https://doi.org/10.1109/34.1000236
"""

def euclidean_distance(point_a: list[float], point_b: list[float]) -> float:
    """Compute the Euclidean distance between two n-dimensional points."""
    if len(point_a) != len(point_b):
        raise ValueError('Both points must have the same number of dimensions.')
    return sum(((a - b) ** 2 for a, b in zip(point_a, point_b))) ** 0.5

def get_points_within_bandwidth(data: list[list[float]], center: list[float], bandwidth: float) -> list[list[float]]:
    """Return all points in data that lie within `bandwidth` distance of `center`."""
    return [point for point in data if euclidean_distance(point, center) <= bandwidth]

def compute_mean(points: list[list[float]]) -> list[float]:
    """Compute the element-wise mean of a list of points."""
    if not points:
        raise ValueError('Cannot compute mean of empty list.')
    n_dims = len(points[0])
    return [sum((point[dim] for point in points)) / len(points) for dim in range(n_dims)]

def shift_point(point: list[float], data: list[list[float]], bandwidth: float) -> list[float]:
    """Shift a single point to the mean of all data points within `bandwidth`.

    If no points fall within the bandwidth, the point remains unchanged."""
    neighbors = get_points_within_bandwidth(data, point, bandwidth)
    if not neighbors:
        return point
    return compute_mean(neighbors)

def has_converged(old_point: list[float], new_point: list[float], tolerance: float) -> bool:
    """Check whether a point has converged (moved less than `tolerance`)."""
    return euclidean_distance(old_point, new_point) < tolerance

def merge_centroids(centroids: list[list[float]], bandwidth: float) -> list[list[float]]:
    """Merge centroids that are within `bandwidth` distance of each other.

    Iterates through centroids and greedily merges any that are close enough,
    keeping the first encountered as the representative."""
    merged: list[list[float]] = []
    for centroid in centroids:
        if all((euclidean_distance(centroid, existing) >= bandwidth for existing in merged)):
            merged.append(centroid)
    return merged

def mean_shift(data: list[list[float]], bandwidth: float, max_iterations: int=300, tolerance: float=0.0001) -> list[int]:
    """Perform Mean Shift clustering on a dataset.

    Args:
        data:           List of n-dimensional data points.
        bandwidth:      Radius of the window used to compute the mean.
                        Must be greater than 0.
        max_iterations: Maximum number of shift iterations per point.
                        Must be at least 1.
        tolerance:      Convergence threshold — stop shifting when movement
                        is smaller than this value. Must be greater than 0.

    Returns:
        A list of integer cluster labels, one per input point.
        Cluster IDs start from 0.

    Raises:
        ValueError: If data is empty.
        ValueError: If bandwidth is not positive.
        ValueError: If max_iterations is less than 1.
        ValueError: If tolerance is not positive.

    Example — two well-separated clusters:"""
    if not data:
        raise ValueError('Data must not be empty.')
    if bandwidth <= 0:
        raise ValueError('Bandwidth must be greater than 0.')
    if max_iterations < 1:
        raise ValueError('max_iterations must be at least 1.')
    if tolerance <= 0:
        raise ValueError('Tolerance must be greater than 0.')
    candidates = [point[:] for point in data]
    for _ in range(max_iterations):
        new_candidates = [shift_point(candidate, data, bandwidth) for candidate in candidates]
        if all((has_converged(old, new, tolerance) for old, new in zip(candidates, new_candidates))):
            break
        candidates = new_candidates
    centroids = merge_centroids(candidates, bandwidth)
    labels = [min(range(len(centroids)), key=lambda centroid_index: euclidean_distance(point, centroids[centroid_index])) for point in data]
    return labels