from collections import deque

class Process:

    def __init__(self, process_name: str, arrival_time: int, burst_time: int) -> None:
        self.process_name = process_name
        self.arrival_time = arrival_time
        self.stop_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

class MLFQ:
    """
    MLFQ(Multi Level Feedback Queue)
    https://en.wikipedia.org/wiki/Multilevel_feedback_queue
    MLFQ has a lot of queues that have different priority
    In this MLFQ,
    The first Queue(0) to last second Queue(N-2) of MLFQ have Round Robin Algorithm
    The last Queue(N-1) has First Come, First Served Algorithm
    """

    def __init__(self, number_of_queues: int, time_slices: list[int], queue: deque[Process], current_time: int) -> None:
        self.number_of_queues = number_of_queues
        self.time_slices = time_slices
        self.ready_queue = queue
        self.current_time = current_time
        self.finish_queue: deque[Process] = deque()

    def calculate_sequence_of_finish_queue(self) -> list[str]:
        """This method returns the sequence of finished processes"""
        sequence = []
        for i in range(len(self.finish_queue)):
            sequence.append(self.finish_queue[i].process_name)
        return sequence

    def calculate_waiting_time(self, queue: list[Process]) -> list[int]:
        """This method calculates waiting time of processes"""
        waiting_times = []
        for i in range(len(queue)):
            waiting_times.append(queue[i].waiting_time)
        return waiting_times

    def calculate_turnaround_time(self, queue: list[Process]) -> list[int]:
        """This method calculates turnaround time of processes"""
        turnaround_times = []
        for i in range(len(queue)):
            turnaround_times.append(queue[i].turnaround_time)
        return turnaround_times

    def calculate_completion_time(self, queue: list[Process]) -> list[int]:
        """This method calculates completion time of processes"""
        completion_times = []
        for i in range(len(queue)):
            completion_times.append(queue[i].stop_time)
        return completion_times

    def calculate_remaining_burst_time_of_processes(self, queue: deque[Process]) -> list[int]:
        """This method calculate remaining burst time of processes"""
        return [q.burst_time for q in queue]

    def update_waiting_time(self, process: Process) -> int:
        """This method updates waiting times of unfinished processes"""
        process.waiting_time += self.current_time - process.stop_time
        return process.waiting_time

    def first_come_first_served(self, ready_queue: deque[Process]) -> deque[Process]:
        """FCFS(First Come, First Served)
        FCFS will be applied to MLFQ's last queue
        A first came process will be finished at first"""
        finished: deque[Process] = deque()
        while len(ready_queue) != 0:
            cp = ready_queue.popleft()
            if self.current_time < cp.arrival_time:
                self.current_time += cp.arrival_time
            self.update_waiting_time(cp)
            self.current_time += cp.burst_time
            cp.burst_time = 0
            cp.turnaround_time = self.current_time - cp.arrival_time
            cp.stop_time = self.current_time
            finished.append(cp)
        self.finish_queue.extend(finished)
        return finished

    def round_robin(self, ready_queue: deque[Process], time_slice: int) -> tuple[deque[Process], deque[Process]]:
        """RR(Round Robin)
        RR will be applied to MLFQ's all queues except last queue
        All processes can't use CPU for time more than time_slice
        If the process consume CPU up to time_slice, it will go back to ready queue"""
        finished: deque[Process] = deque()
        for _ in range(len(ready_queue)):
            cp = ready_queue.popleft()
            if self.current_time < cp.arrival_time:
                self.current_time += cp.arrival_time
            self.update_waiting_time(cp)
            if cp.burst_time > time_slice:
                self.current_time += time_slice
                cp.burst_time -= time_slice
                cp.stop_time = self.current_time
                ready_queue.append(cp)
            else:
                self.current_time += cp.burst_time
                cp.burst_time = 0
                cp.stop_time = self.current_time
                cp.turnaround_time = self.current_time - cp.arrival_time
                finished.append(cp)
        self.finish_queue.extend(finished)
        return (finished, ready_queue)

    def multi_level_feedback_queue(self) -> deque[Process]:
        """MLFQ(Multi Level Feedback Queue)"""
        for i in range(self.number_of_queues - 1):
            _finished, self.ready_queue = self.round_robin(self.ready_queue, self.time_slices[i])
        self.first_come_first_served(self.ready_queue)
        return self.finish_queue