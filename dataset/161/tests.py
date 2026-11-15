import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert euclidean_distance([0.0, 0.0], [3.0, 4.0]) == 5.0
    assert euclidean_distance([1.0, 1.0], [1.0, 1.0]) == 0.0
    assert euclidean_distance([0.0], [5.0]) == 5.0
    data = [[0.0, 0.0], [0.5, 0.5], [5.0, 5.0]]
    assert get_points_within_bandwidth(data, [0.0, 0.0], 1.0) == [[0.0, 0.0], [0.5, 0.5]]
    assert get_points_within_bandwidth(data, [5.0, 5.0], 1.0) == [[5.0, 5.0]]
    assert get_points_within_bandwidth(data, [0.0, 0.0], 10.0) == [[0.0, 0.0], [0.5, 0.5], [5.0, 5.0]]
    assert compute_mean([[1.0, 2.0], [3.0, 4.0]]) == [2.0, 3.0]
    assert compute_mean([[0.0, 0.0, 0.0]]) == [0.0, 0.0, 0.0]
    data = [[1.0, 1.0], [1.5, 1.5], [10.0, 10.0]]
    assert shift_point([1.0, 1.0], data, 2.0) == [1.25, 1.25]
    assert shift_point([10.0, 10.0], data, 1.0) == [10.0, 10.0]
    assert has_converged([1.0, 1.0], [1.0000001, 1.0000001], 1e-4) == True
    assert has_converged([1.0, 1.0], [1.5, 1.5], 1e-4) == False
    centroids = [[1.0, 1.0], [1.1, 1.1], [10.0, 10.0]]
    merged = merge_centroids(centroids, 1.0)
    assert len(merged) == 2
    centroids = [[0.0, 0.0], [5.0, 5.0], [10.0, 10.0]]
    assert len(merge_centroids(centroids, 1.0)) == 3
    data = [
    [1.0, 1.0], [1.2, 1.0], [1.0, 1.2],
    [9.0, 9.0], [9.2, 9.0], [9.0, 9.2],
]
    labels = mean_shift(data, bandwidth=2.0)
    assert len(set(labels))  # two clusters == 2
    assert labels[0] == labels[1] == labels[2]  # first group same cluster == True
    assert labels[3] == labels[4] == labels[5]  # second group same cluster == True
    assert labels[0] != labels[3]               # different clusters == True
    data = [[0.0, 0.0], [0.1, 0.0], [0.0, 0.1], [0.1, 0.1]]
    labels = mean_shift(data, bandwidth=2.0)
    assert len(set(labels)) == 1
