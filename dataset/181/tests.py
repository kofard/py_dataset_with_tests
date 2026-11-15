import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
    _ = mlfq.multi_level_feedback_queue()
    assert mlfq.calculate_sequence_of_finish_queue() == ['P2', 'P4', 'P1', 'P3']
    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
    _ = mlfq.multi_level_feedback_queue()
    assert mlfq.calculate_waiting_time([P1, P2, P3, P4]) == [83, 17, 94, 101]
    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
    _ = mlfq.multi_level_feedback_queue()
    assert mlfq.calculate_turnaround_time([P1, P2, P3, P4]) == [136, 34, 162, 125]
    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
    _ = mlfq.multi_level_feedback_queue()
    assert mlfq.calculate_completion_time([P1, P2, P3, P4]) == [136, 34, 162, 125]
    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
    finish_queue, ready_queue = mlfq.round_robin(deque([P1, P2, P3, P4]), 17)
    assert mlfq.calculate_remaining_burst_time_of_processes(mlfq.finish_queue) == [0]
    assert mlfq.calculate_remaining_burst_time_of_processes(ready_queue) == [36, 51, 7]
    finish_queue, ready_queue = mlfq.round_robin(ready_queue, 25)
    assert mlfq.calculate_remaining_burst_time_of_processes(mlfq.finish_queue) == [0, 0]
    assert mlfq.calculate_remaining_burst_time_of_processes(ready_queue) == [11, 26]
    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
    mlfq.current_time = 10
    P1.stop_time = 5
    assert mlfq.update_waiting_time(P1) == 5
    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
    _ = mlfq.first_come_first_served(mlfq.ready_queue)
    assert mlfq.calculate_sequence_of_finish_queue() == ['P1', 'P2', 'P3', 'P4']
    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
    finish_queue, ready_queue = mlfq.round_robin(mlfq.ready_queue, 17)
    assert mlfq.calculate_sequence_of_finish_queue() == ['P2']
    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
    finish_queue = mlfq.multi_level_feedback_queue()
    assert mlfq.calculate_sequence_of_finish_queue() == ['P2', 'P4', 'P1', 'P3']
