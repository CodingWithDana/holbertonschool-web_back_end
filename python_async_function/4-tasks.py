#!/usr/bin/env python3
"""
Module that provides a function to run multiple asynchronous tasks using task_wait_random
"""


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait(n: int, max_delay: int) -> List[float]:
    """
    Run multiple asynchronous tasks that wait for a random delay and return results
    in the order of completion
    """
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    result = []
    for completed_coroutines in asyncio.as_completed(coroutines):
        delay = await completed_coroutines
        result.append(delay)
    return result
