#!/usr/bin/env python3
"""
Module that provides a function index_range to return a tuple of size two.
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination

    page (int): The current page number (1-indexed).
    page_size (int): The number of items per page.

    Examples:
    >>> index_range(1, 10)
    (0, 10)
    >>> index_range(3, 5)
    (10, 15)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
