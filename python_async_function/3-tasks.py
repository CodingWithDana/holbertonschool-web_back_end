#!/usr/bin/env python3
"""
Module that provides a function (regular function) to take an int and 
return a asyncio.Task
"""


import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task from the wait_random coroutine with the given delay
    """
    coroutine = wait_random(max_delay)
    task = asyncio.create_task(coroutine)
    return task
