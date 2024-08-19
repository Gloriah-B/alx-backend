#!/usr/bin/env python3
"""
This module provides a Server class to paginate database of popular baby names
"""


import csv
import os
from typing import List, Tuple

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = 'Popular_Baby_Names.csv'

    def __init__(self):
        """Initialize instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset.

        Loads the dataset from a CSV file if it hasn't been loaded yet.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, mode='r') as f:
                    reader = csv.reader(f)
                    dataset = [row for row in reader]
                   self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset. """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        indices = index_range(page, page_size)
        start = indices[0]
        end = indices[1]

        try:
            return self.dataset()[start:end]
        except IndexError:
            return []
