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
            if not os.path.exists(self.DATA_FILE):
                raise FileNotFoundError(f"File not found: {self.DATA_FILE}")

            try:
                with open(self.DATA_FILE, mode='r') as f:
                    reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
            except FileNotFoundError:
                raise FileNotFoundError(
                            f"Could not open file: {self.DATA_FILE}"
                                        )
            except Exception as e:
                raise Exception(f"An error occurred while reading file:{e}")
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: The appropriate page of the dataset.
        """
        assert isinstance(page, int) and page > 0, (
                                            "Page must be a positive integer."
                                                    )
        assert isinstance(page_size, int) and page_size > 0, (
                                    "Page size must be a positive integer."
                                                            )

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        # Return an empty list if the start index is out of range
        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
