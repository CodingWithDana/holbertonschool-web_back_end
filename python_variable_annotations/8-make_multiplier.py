#!/usr/bin/env python3
"""
Module that provides a function to take a float multiplier as argument
and return a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function that multiplies a float by a given multiplier
    """
    def callable_function(a: float) -> float:
        """ Multiply input a by the multiplier """
        return a * multiplier
    return callable_function
