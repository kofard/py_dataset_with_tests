import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    cq = CircularQueueLinkedList(2)
    cq.enqueue('a')
    cq.enqueue('b')
    cq = CircularQueueLinkedList()
    assert cq.is_empty() == True
    cq.enqueue('a')
    assert cq.is_empty() == False
    assert cq.dequeue() == 'a'
    assert cq.is_empty() == True
    cq = CircularQueueLinkedList()
    cq.enqueue('a')
    assert cq.first() == 'a'
    assert cq.dequeue() == 'a'
    cq.enqueue('b')
    cq.enqueue('c')
    assert cq.first() == 'b'
    cq = CircularQueueLinkedList()
    cq.enqueue('a')
    cq.enqueue('b')
    assert cq.dequeue() == 'a'
    assert cq.dequeue() == 'b'
    cq = CircularQueueLinkedList()
    cq.enqueue('a')
    assert cq.dequeue() == 'a'
