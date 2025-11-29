#!/usr/bin/env python3
"""
Module that provides a function to measure the total execution time
for wait_n and return total_time/n
"""


import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for all the coroutines to complete
    and returns the average execution time per coroutine
    """
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()
    return (end - start) / n
