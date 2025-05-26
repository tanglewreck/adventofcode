"""
    utils.py
    --------
        Utility functions for the Advent of Code project

    author
    ------
        mier

    date
    -----
        2025-05-26

"""

# pylint: disable=unused-import
import re
from string import digits
from typing import List, Callable
import numpy as np
import pandas as pd
# pylint: enable=unused-import


def mul(x: int|float, y: int|float) -> int|float:
    """Multiply two numbers"""
    return x * y


def get_token(data_string: str, index: int, length: int) -> str:
    """
        get_token()
            Return a substring of length 'length' beginning at 'index'.
    """
    try:
        return data_string[index : index + length]
    except IndexError:
        return ""
