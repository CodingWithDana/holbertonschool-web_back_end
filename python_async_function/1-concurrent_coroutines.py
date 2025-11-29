#!/usr/bin/env python3
"""
Module that provides an async routine to run wait_random multiple
times concurrently
"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run wait_random n times concurrently and return delays in ascending order
    without using sort()
    """

    coroutines = [wait_random(max_delay) for _ in range(n)]

    results = []

    for completed_coroutines in asyncio.as_completed(coroutines):
        delay = await completed_coroutines
        results.append(delay)
    return results
