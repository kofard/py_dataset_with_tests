import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    costs, operations = compute_transform_tables("cat", "cut", 1, 2, 3, 3)
    assert costs[0][:4] == [0, 3, 6, 9]
    assert costs[2][:4] == [6, 4, 3, 6]
    assert operations[0][:4] == ['0', 'Ic', 'Iu', 'It']
    assert operations[3][:4] == ['Dt', 'Dt', 'Rtu', 'Ct']
    assert compute_transform_tables("", "", 1, 2, 3, 3) == ([[0]], [['0']])
    ops = [['0', 'Ic', 'Iu', 'It'],
       ['Dc', 'Cc', 'Iu', 'It'],
       ['Da', 'Da', 'Rau', 'Rat'],
       ['Dt', 'Dt', 'Rtu', 'Ct']]
    x = len(ops) - 1
    y = len(ops[0]) - 1
    assert assemble_transformation(ops, x, y) == ['Cc', 'Rau', 'Ct']
    assert assemble_transformation(ops, x, y-1) == ['Cc', 'Da', 'Rtu']
    ops1 = [['0']]
    x1 = len(ops1) - 1
    y1 = len(ops1[0]) - 1
    assert assemble_transformation(ops1, x1, y1) == []
    ops2 = [['0', 'I1', 'I2', 'I3'],
        ['D1', 'C1', 'I2', 'I3'],
        ['D2', 'D2', 'R23', 'R23']]
    x2 = len(ops2) - 1
    y2 = len(ops2[0]) - 1
    assert assemble_transformation(ops2, x2, y2) == ['C1', 'I2', 'R23']
