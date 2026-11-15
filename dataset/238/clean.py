"""
Round Robin is a scheduling algorithm.
In Round Robin each process is assigned a fixed time slot in a cyclic way.
https://en.wikipedia.org/wiki/Round-robin_scheduling
"""
from __future__ import annotations
from statistics import mean

def calculate_waiting_times(burst_times: list[int]) -> list[int]:
    """Calculate the waiting times of a list of processes that have a specified duration.

    Return: The waiting time for each process."""
    quantum = 2
    rem_burst_times = list(burst_times)
    waiting_times = [0] * len(burst_times)
    t = 0
    while True:
        done = True
        for i, burst_time in enumerate(burst_times):
            if rem_burst_times[i] > 0:
                done = False
                if rem_burst_times[i] > quantum:
                    t += quantum
                    rem_burst_times[i] -= quantum
                else:
                    t += rem_burst_times[i]
                    waiting_times[i] = t - burst_time
                    rem_burst_times[i] = 0
        if done is True:
            return waiting_times

def calculate_turn_around_times(burst_times: list[int], waiting_times: list[int]) -> list[int]:
    return [burst + waiting for burst, waiting in zip(burst_times, waiting_times)]