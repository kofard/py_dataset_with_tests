import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert SegmentTree([1, 2, 3], lambda a, b: a + b).query(0, 2) == 6
    assert SegmentTree([3, 1, 2], min).query(0, 2) == 1
    assert SegmentTree([2, 3, 1], max).query(0, 2) == 3
    st = SegmentTree([1, 5, 7, -1, 6], lambda a, b: a + b)
    st.update(1, -1)
    st.update(2, 3)
    assert st.query(1, 2) == 2
    assert st.query(1, 1) == -1
    st.update(4, 1)
    assert st.query(3, 4) == 0
    st = SegmentTree([[1, 2, 3], [3, 2, 1], [1, 1, 1]], lambda a, b: [a[i] + b[i] for i
                                                                  in range(len(a))])
    assert st.query(0, 1) == [4, 4, 4]
    assert st.query(1, 2) == [4, 3, 2]
    st.update(1, [-1, -1, -1])
    assert st.query(1, 2) == [0, 0, 0]
    assert st.query(0, 2) == [1, 2, 3]
    assert SegmentTree(['a', 'b', 'c'], lambda a, b: f'{a}{b}').query(0, 2) == 'abc'
    assert SegmentTree([(1, 2), (2, 3), (3, 4)],
            lambda a, b: (a[0] + b[0], a[1] + b[1])).query(0, 2) == (6, 9)
    st = SegmentTree([3, 1, 2, 4], min)
    assert st.query(0, 3) == 1
    st.update(2, -1)
    assert st.query(0, 3) == -1
    st = SegmentTree([1, 2, 3, 4], lambda a, b: a + b)
    assert st.query(0, 2) == 6
    assert st.query(1, 2) == 5
    assert st.query(0, 3) == 10
    assert st.query(2, 3) == 7
