#!/usr/bin/env python3
"""
Module that provide a function to return values with the appropriate types
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples where each tuple has an element from the input
    iterable and its length
    """
    return [(i, len(i)) for i in lst]
