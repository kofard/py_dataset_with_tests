import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]
    init = [0, 0]
    goal = [len(grid) - 1, len(grid[0]) - 1]
    cost = 1
    heuristic = [[0] * len(grid[0]) for _ in range(len(grid))]
    heuristic = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            heuristic[i][j] = abs(i - goal[0]) + abs(j - goal[1])
            if grid[i][j] == 1:
                heuristic[i][j] = 99
    path, action = search(grid, init, goal, cost, heuristic)
    assert path  == [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [4, 1], [4, 2], [4, 3], [3, 3], [2, 3], [2, 4], [2, 5], [3, 5], [4, 5]]
    assert action  == [[0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0], [2, 0, 0, 0, 3, 3], [2, 0, 0, 0, 0, 2], [2, 3, 3, 3, 0, 2]]
