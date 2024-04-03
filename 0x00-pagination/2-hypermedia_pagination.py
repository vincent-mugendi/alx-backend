#!/usr/bin/env python3
""" Simple helper function """
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    The function should return a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to return in a list for
    those particular pagination parameters.

    Arguments:
    page: integer
    page_size: integer
    """
    start_index = (page * page_size) - page_size
    end_index = start_index + page_size
    return(start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        find the correct indexes to paginate the dataset correctly and
        return the appropriate page of the dataset

        Arguments:
        page: integer
        page_size: integer
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        index = index_range(page, page_size)
        start = index[0]
        end = index[1]
        data = self.dataset()
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        find the correct indexes to paginate the dataset correctly and
        return the appropriate page of the dataset in a dictionary

        Arguments:
        page: integer
        page_size: integer
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        pages = index_range(page, page_size)
        start, end = pages[0], pages[1]
        page_size = end - start
        next_page = page + 1
        if next_page > len(data):
            next_page = None
        prev_page = page - 1
        if prev_page < 1:
            prev_page = None
        page_size
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
