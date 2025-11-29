#!/usr/bin/env python3
"""
    Module that provides a coroutine that generates 10 random numbers
    between 0 and 10, generating one every second asynchronously
"""


import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generate asynchronously 10 random numbers betwen 0 and 10

    This coroutine loops 10 times. On each iteration, it asynchronously waits
    for 1 second, generates a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        random_number = uniform(0, 10)
        yield random_number
