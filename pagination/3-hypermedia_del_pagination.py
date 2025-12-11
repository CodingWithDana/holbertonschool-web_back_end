#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Optional


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a page of data indexed by the starting position, resilient
        to deletions

        Args:
            index (int, optional): The current start index of the page.
            Defaults to 0 if None.
            page_size (int, optional): The number of items to return in
            the page. Defaults to 10.

        Returns:
        dict: A dictionary containing:
            'index' (int): The current start index.
            'next_index' (Optional[int]): The next start index for pagination
                or None if no more data.
            'page_size' (int): The number of items returned.
            'data' (List[List]): The list of dataset rows for the current page.
        """
        if index is None:
            index = 0

        dataset = self.indexed_dataset()
        keys = sorted(dataset.keys())

        assert isinstance(index, int)
        assert 0 <= index < len(keys)

        start_position = None
        for position, key in enumerate(keys):
            if key >= index:
                start_position = position
                break

        if start_position is None:
            return None

        page_keys = keys[start_position:start_position + page_size]
        data = [dataset[k] for k in page_keys]

        if start_position + page_size < len(keys):
            next_index = keys[start_position + page_size]
        else:
            next_index = None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
