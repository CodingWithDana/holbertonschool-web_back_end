#!/usr/bin/env python3
"""
Module that provides a coroutine to collect 10 random numbers using
imported async_generator function
then return the 10 random numbers
"""


from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously collect 10 random numbers
    """
    result = [numbers async for numbers in async_generator()]
    return result
