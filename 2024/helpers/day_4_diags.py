# coding: utf-8
"""
    Extract diagonals:
        - downwards, going left-to-right
        - downwards, going right-to-left
"""

__all__ = ["lower_left_diagonals",
           "lower_right_diagonals",
           "upper_left_diagonals",
           "upper_right_diagonals",
           "extract_diagonals",
           "DF", "N"]
__author__ = "mier"
__version__ = "0.4.42"


# pylint: disable=unused-import
from typing import Any, Optional, TYPE_CHECKING
import numpy as np
import pandas as pd
# pylint: enable=unused-import
from . import __DATADIR__

try:
    DF = pd.read_csv(f"{__DATADIR__}/day_4_data_example.csv", header=None)
    N = len(DF)
except pd.errors.EmptyDataError as exception:
    print(f"WARNING: {repr(exception)}")


def lower_left_diagonals(df: pd.DataFrame | None = None,
                         start: int | None = None,
                         stop: int | None = -1) -> list:  # mypy: no-operator
    """
        lower_left_diagonals():
            Extract diagonals starting at the
            lower-right corner and going down-left;
            i.e. start in the lower-right corner, moving up,
            extract diagonals starting at (k, n - 1),
            for k = (n-1), (n-1), ... , 0.

    """
    d = np.asarray(df)
    # Flip the array left-right so that we
    # can use np.diagonal().
    dflip = np.fliplr(d)
    n = len(df)  # mypy: no-arg-type
    # Amend start position (row)
    if start is None:
        start = n - 1
    diags = []
    for k in range(start, stop, -1):
        diag = dflip[k:n, 0:(n - k)].diagonal()
        diags.append(diag)
    return diags


def lower_right_diagonals(df: pd.DataFrame | None = None,
                          start: int | None = None,
                          stop: int | None = None) -> list:
    """
        lower_right_diagonals()
            Extract diagonals starting at the
            lower-left corner and going down-right,
            i.e. start in the lower-left corner, moving up,
            extract diagonals starting at (k, 0),
            for k = (n-1), (n-1), ... , 0.
    """
    # Convert to np.ndarray so we can use np.diagonal()
    d = np.asarray(df)
    n = len(d)
    # To extract all diagonals, we would start at the
    # lower-left corner,i.e. at (0, n - 1), but since
    # we will be looking for the string 'XMAS' there's
    # no use in partitioning the data into smaller chunks
    # than 4 by 4. So, unless explicitly being told otherwise,
    # start at (n - 4, 0), extracting a 4 x 4 partion.
    # Amend start position (row)
    if start is None:
        start = n - 1
    if stop is None:
        stop = -1
    diags = []
    for row in range(start, stop, -1):
        diag = d[row:n, 0:(n - row)].diagonal()
        diags.append(diag)
    return diags


def upper_right_diagonals(df: pd.DataFrame | None = None,
                          start: int | None = None,
                          stop: int | None = None) -> list:
    """
        upper_right_diagonals():
            Extract diagonals starting at the upper-right corner
            and going down-right,
            i.e. start in the upper-right corner, moving down,
            extract diagonals starting at (0, k),
            for k = (n-1), (n-1), ... , 1. Since we want to use
            np.diagonal(), which returns the diagonal starting
            top-left and going down-right, we need to transform
            the data by reversing the rows; for this we use
            np.fliplr(), which is equivalent to
            [row[::-1] for row in d]. Therefore, when processing
            the transformed matrix, k = 0, 1, ... , n - 1, or
            rather, since we will be looking for the string 'XMAS',
            k = 4, ... , n - 1.

    """
    # Get length of the data
    n = len(df)
    # Amend start and stop positions (rows)
    if start is None:
        start = 1
    if stop is None:
        stop = len(df)
    # convert to np.ndarray
    d = np.asarray(df)
    # then flip it left-right
    # (equivalent to [r[::-1] for r in d]).
    dflip = np.fliplr(d)
    # then flip it upside-down
    # (equivalent to dflip[::-1]);
    # the upper-right corner is now
    # at the bottom-left
    dflipud = np.flipud(dflip)
    # now, use lower_right_diagonals() to
    # extract the diagonals (they will come
    # out being reverse-sorted, but that's ok)
    df_flipud = pd.DataFrame(dflipud)
    return lower_right_diagonals(df_flipud, n - start, n - stop)


def upper_left_diagonals(df: pd.DataFrame | None = None,
                         start: int | None = None,
                         stop: int | None = None) -> list:
    """
        upper-left_diagonals():
            Extract diagonals starting at the upper-left corner
            and going down-left,
            i.e. start in the upper-left corner, moving down,
            extract diagonals starting at (0, k),
            for k = (n-1), (n-1), ... , 0.
            i.e. start in the upper-right corner, moving down,
            extract diagonals starting at (0, k),
            for k = (n-1), (n-1), ... , 1. Since we want to use
            np.diagonal(), which returns the diagonal starting
            top-left and going down-right, we need to transform
            the data by reversing the rows; for this we use
            np.fliplr(), which is equivalent to
            [row[::-1] for row in d]. Therefore, when processing
            the transformed matrix, k = 0, 1, ... , n - 1, or
            rather, since we will be looking for the string 'XMAS',
            k = 4, ... , n - 1.

    """
    d = np.asarray(df)
    # Amend stop position (row)
    if start is None:
        start = 1
    if stop is None:
        stop = len(df)
    diags = []
    for k in range(start, stop):
        diag = d[:k, :k][::-1].diagonal()[::-1]
        diags.append(diag)
    return diags


def extract_diagonals(df):
    """Extract diagonals from a dataframe"""
    diagonals = lower_left_diagonals(df)
    diagonals += upper_left_diagonals(df)
    diagonals += upper_right_diagonals(df)
    diagonals += lower_right_diagonals(df)
    return diagonals
