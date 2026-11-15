from __future__ import annotations

def calculate_waiting_times(duration_times: list[int]) -> list[int]:
    """This function calculates the waiting time of some processes that have a
    specified duration time.
        Return: The waiting time for each process."""
    waiting_times = [0] * len(duration_times)
    for i in range(1, len(duration_times)):
        waiting_times[i] = duration_times[i - 1] + waiting_times[i - 1]
    return waiting_times

def calculate_turnaround_times(duration_times: list[int], waiting_times: list[int]) -> list[int]:
    """This function calculates the turnaround time of some processes.
        Return: The time difference between the completion time and the
                arrival time.
                Practically waiting_time + duration_time"""
    return [duration_time + waiting_times[i] for i, duration_time in enumerate(duration_times)]

def calculate_average_turnaround_time(turnaround_times: list[int]) -> float:
    """This function calculates the average of the turnaround times
        Return: The average of the turnaround times."""
    return sum(turnaround_times) / len(turnaround_times)

def calculate_average_waiting_time(waiting_times: list[int]) -> float:
    """This function calculates the average of the waiting times
        Return: The average of the waiting times."""
    return sum(waiting_times) / len(waiting_times)