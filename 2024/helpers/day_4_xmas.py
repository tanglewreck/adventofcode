# coding: utf-8
"""
    day_4_pt2
"""
import pandas as pd
import numpy as np
from . import __DATADIR__


__all__ = ["x_mas_list", "x_mas_pd", "x_mas_np"]

# These determine, e.g., which data file is read
__DAYNUM__ = "day_4"  # this is day 4
__PART__ = "2"  # this is part 2 of day 4

DF4E = pd.read_csv(f"{__DATADIR__}/day_4_part_2_example.csv", header=None)
DF4F = pd.read_csv(f"{__DATADIR__}/day_4_part_1.csv", header=None)


# pylint: disable=line-too-long
def x_mas_pd(df: pd.DataFrame | None):
    """
        Find X-MAS patterns, pandas version
    """
    if df is None:
        df = DF4F
    n = len(df)
    count = 0
    for row in range(n):
        for col in range(n):
            # This test is necessary since using try-except to try to just
            # ignore when we try to fetch outside the grid results in the
            # count being to large (2006 instead of 2003), which is kind of
            # odd; you would expect it to work, but it doesn't and I don't
            # understand why (so far).
            #
            # The alternative is looping over (1:n-1, 1:n-1) instead of the
            # full range, but that means making assumptions about the data
            # (it's size/shape) and this I do not like, for some reason. I
            # mean, it SHOULD work damnit!
            if row == 0 or row == n-1 or col == 0 or col == n-1:
                continue
            if df.iloc[row, col] == 'A':
                try:
                    if ((df.iloc[row-1, col-1] == "M" and df.iloc[row-1, col+1] == "S") and
                        (df.iloc[row+1, col-1] == "M" and df.iloc[row+1, col+1] == "S")):
                        count += 1
                    if ((df.iloc[row-1, col-1] == "M" and df.iloc[row-1, col+1] == "M") and
                        (df.iloc[row+1, col-1] == "S" and df.iloc[row+1, col+1] == "S")):
                        count += 1
                    if ((df.iloc[row-1, col-1] == "S" and df.iloc[row-1, col+1] == "S") and
                        (df.iloc[row+1, col-1] == "M" and df.iloc[row+1, col+1] == "M")):
                        count += 1
                    if ((df.iloc[row-1, col-1] == "S" and df.iloc[row-1, col+1] == "M") and
                        (df.iloc[row+1, col-1] == "S" and df.iloc[row+1, col+1] == "M")):
                        count += 1
                except IndexError:
                    pass
    return count


def x_mas_np(df: pd.DataFrame | None):
    """
        Find X-MAS patterns, numpy version
    """
    if df is None:
        df = DF4F
    rows = np.asarray(df)
    n = len(rows)
    count = 0
    for row in range(n):
        for col in range(n):
            if row == 0 or row == n-1 or col == 0 or col == n-1:
                continue
            if rows[row][col] == 'A':
                if ((rows[row-1][col-1] == 'M' and rows[row-1][col+1] == 'M') and
                    (rows[row+1][col-1] == 'S' and rows[row+1][col+1] == 'S')):
                    count += 1
                if ((rows[row-1][col-1] == 'M' and rows[row-1][col+1] == 'S') and
                    (rows[row+1][col-1] == 'M' and rows[row+1][col+1] == 'S')):
                    count += 1
                if ((rows[row-1][col-1] == 'S' and rows[row-1][col+1] == 'M') and
                    (rows[row+1][col-1] == 'S' and rows[row+1][col+1] == 'M')):
                    count += 1
                if ((rows[row-1][col-1] == 'S' and rows[row-1][col+1] == 'S') and
                    (rows[row+1][col-1] == 'M' and rows[row+1][col+1] == 'M')):
                    count += 1
    return count


def x_mas_list(df: pd.DataFrame | None):
    """
        Find X-MAS patterns, list version
    """
    if df is None:
        df = DF4F
    rows = [list(row) for row in np.asarray(df)]
    n = len(rows)
    count = 0
    for row in range(1, n-1):
        for col in range(1, n-1):
            if rows[row][col] == 'A':
                if ((rows[row-1][col-1] == 'M' and rows[row-1][col+1] == 'M') and
                    (rows[row+1][col-1] == 'S' and rows[row+1][col+1] == 'S')):
                    count += 1
                if ((rows[row-1][col-1] == 'M' and rows[row-1][col+1] == 'S') and
                    (rows[row+1][col-1] == 'M' and rows[row+1][col+1] == 'S')):
                    count += 1
                if ((rows[row-1][col-1] == 'S' and rows[row-1][col+1] == 'M') and
                    (rows[row+1][col-1] == 'S' and rows[row+1][col+1] == 'M')):
                    count += 1
                if ((rows[row-1][col-1] == 'S' and rows[row-1][col+1] == 'S') and
                    (rows[row+1][col-1] == 'M' and rows[row+1][col+1] == 'M')):
                    count += 1
    return count
