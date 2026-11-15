"""
Non-preemptive Shortest Job First
Shortest execution time process is chosen for the next execution.
https://www.guru99.com/shortest-job-first-sjf-scheduling.html
https://en.wikipedia.org/wiki/Shortest_job_next
"""
from __future__ import annotations
from statistics import mean

def calculate_waitingtime(arrival_time: list[int], burst_time: list[int], no_of_processes: int) -> list[int]:
    """Calculate the waiting time of each processes

    Return: The waiting time for each process."""
    waiting_time = [0] * no_of_processes
    remaining_time = [0] * no_of_processes
    for i in range(no_of_processes):
        remaining_time[i] = burst_time[i]
    ready_process: list[int] = []
    completed = 0
    total_time = 0
    while completed != no_of_processes:
        ready_process = []
        target_process = -1
        for i in range(no_of_processes):
            if arrival_time[i] <= total_time and remaining_time[i] > 0:
                ready_process.append(i)
        if len(ready_process) > 0:
            target_process = ready_process[0]
            for i in ready_process:
                if remaining_time[i] < remaining_time[target_process]:
                    target_process = i
            total_time += burst_time[target_process]
            completed += 1
            remaining_time[target_process] = 0
            waiting_time[target_process] = total_time - arrival_time[target_process] - burst_time[target_process]
        else:
            total_time += 1
    return waiting_time

def calculate_turnaroundtime(burst_time: list[int], no_of_processes: int, waiting_time: list[int]) -> list[int]:
    """Calculate the turnaround time of each process.

    Return: The turnaround time for each process."""
    turn_around_time = [0] * no_of_processes
    for i in range(no_of_processes):
        turn_around_time[i] = burst_time[i] + waiting_time[i]
    return turn_around_time