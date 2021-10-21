from collections import deque
from sys import maxsize


def calculate_needed_jobs(jobs: deque, job_i: int, current_i=None, clocks=0):
    if current_i == job_i:
        return clocks

    current_i = jobs.index(min(jobs))
    clocks += jobs[current_i]
    jobs[current_i] = maxsize
    return calculate_needed_jobs(jobs, job_i, current_i, clocks)


jobs_data = deque(map(int, input().split(", ")))
job_index = int(input())
print(calculate_needed_jobs(jobs_data, job_index))
