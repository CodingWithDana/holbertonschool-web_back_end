#!/usr/bin/env python3
"""
Module that provides a async function to wait for a random delay and return it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay

    Args:
        max_delay (int): max number of seconds to wait (max is included),
        defaults to 10

    Returns:
        float: the actual delay time waited

    uniform() method: returns a random floating number between
    the two specified numbers (both included)
    """
    # random.uniform(start_of_range, end_of_range) to create a float delay
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)      # for asynchronuous waiting
    return delay
