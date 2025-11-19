#!/usr/bin/env python3
"""
Module that provides a function to take a list `input_list` of floats
as argument
and return their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Calc the sum of a list of floats"""
    return sum(input_list)
