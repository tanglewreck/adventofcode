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
__name__ = "snippets.day_4_4_diags"  # pylint: disable=redefined-bultin
__version__ = "0.4.4"


import numpy as np
import pandas as pd

DF = pd.read_csv("data/day_4_data_example.csv", header=None)
N = len(DF)


def lower_left_diagonals(df: pd.DataFrame = DF,
                         start: int = -1,
                         stop: int = -1) -> list:
    """
        lower_left_diagonals()
            Extract lower-left diagonals going down-right,
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
    # than 4 by 4. In that case, start at (0, n - 4).
    if start == -1:
        start = n - 4
    diags = []
    for row in range(start, stop, -1):
        diag = d[row:n, :n - row].diagonal()
        diags.append(diag)
    return diags


def upper_right_diagonals(df: pd.DataFrame = DF,
                          start: int = -1,
                          stop: int = 0) -> list:
    """
        upper_right_diagonals():
            Extract upper-right diagonals going down-left,
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
    # Convert to np.ndarray
    d = np.asarray(df)
    # then flip it left-right (equivalent to
    # [r[::-1] for r in d]).
    d = np.fliplr(d)
    if start == -1:
        start = 4
    if stop == 0:
        stop = len(df)
    diags = []
    for k in range(start, stop):
        diag = np.fliplr(np.fliplr(d)[:k, :k]).diagonal()
        diags.append(diag)
    return diags


def upper_left_diagonals(df: pd.DataFrame = DF,
                         start=4,
                         stop=0) -> list:
    """
        upper-left_diagonals():
            Extract upper-left diagonals going down-right,
            i.e. start in the upper-left corner, moving down,
            extract diagonals starting at (0, k),
            for k = (n-1), (n-1), ... , 0.
    """
    d = np.asarray(df)
    if stop == 0:
        stop = len(df)
    diags = []
    for k in range(start, stop):
        diag = d[:k, :k][::-1].diagonal()[::-1]
        diags.append(diag)
    return diags


def lower_right_diagonals(df: pd.DataFrame = DF,
                          start:int = N - 4,
                          stop: int = -1) -> list:
    """
        lower_right_diagonals():
            Extract lower-right diagonals going down-right
    """
    d = np.asarray(df)
    # Flip the array left-right so that we
    # use of np.diagonal().
    d = np.fliplr(d)
    n = len(df)
    if start == -1:
        start = n - 4
    diags = []
    for k in range(start, stop, -1):
        diag = d[k:n, :n-k].diagonal()
        diags.append(diag)
    return diags


def extract_diagonals(df):
    """Extract diagonals from a dataframe"""
    diagonals = lower_left_diagonals(df, N - 1)
    diagonals += upper_right_diagonals(df, 1)
    diagonals += upper_left_diagonals(df, 1)
    diagonals += lower_right_diagonals(df, N - 1, -1)
    return diagonals


def main():
    """main()"""
    diags = extract_diagonals(DF)
    for diag in diags:
        print(list(diag))
    print(len(diags))


if __name__ == "__main__":
    main()
