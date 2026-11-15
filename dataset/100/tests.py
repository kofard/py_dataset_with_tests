import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    linked_list = LinkedList()
    assert list(linked_list) == []
    linked_list.add_node(1)
    assert tuple(linked_list) == (1,)
    linked_list = LinkedList()
    linked_list.add_node(1)
    linked_list.add_node(2)
    linked_list.add_node(3)
    linked_list.add_node(4)
    assert tuple(linked_list) == (1, 2, 3, 4)
    linked_list = LinkedList()
    linked_list.add_node(1)
    linked_list.add_node(2)
    linked_list.add_node(3)
    linked_list.add_node(4)
    assert linked_list.detect_cycle() == False
    linked_list.head.next_node.next_node.next_node = linked_list.head.next_node
    assert linked_list.detect_cycle() == True
