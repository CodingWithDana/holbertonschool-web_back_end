#!/usr/bin/env python3
"""
Module that provides a coroutine to execute async_comprehension function 
four times in parallel using asyncio.gather, measure the total runtime
and return the total runtime
"""


import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_time() -> float:
    """
    Measure the total runtime of 4 parallel async comprehensions
    """
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time()
    return end - start
