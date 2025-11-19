#!/usr/bin/env python3
"""
Module that takes a string k and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v and should be annotated as a float
"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Return a tuple with a string and the square of a number as a float """
    return (k, (v ** 2))
