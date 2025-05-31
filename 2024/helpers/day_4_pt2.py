# pylint: disable=all
# coding: utf-8
import pandas as pd
import numpy as np
from . import __DATADIR__

DF4E = pd.read_csv(f"{__DATADIR__}/day_4_part_2_data_example.csv", header=None)
DF4F = pd.read_csv(f"{__DATADIR__}/day_4_data.csv", header=None)


def x_mas_pd(example=False):
    """
        Find X-MAS patterns, pandas version
    """
    if example:
        df = DF4E
    else:
        df = DF4F
    n = len(df)
    count = 0
    for row in range(n):
        for col in range(n):
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
                except IndexError as e:
                    pass
    return count


def x_mas_np(example=False):
    """
        Find X-MAS patterns, numpy version
    """
    if example:
        df = DF4E
    else:
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


def x_mas_list(example=False):
    """
        Find X-MAS patterns, list version
    """
    if example:
        df = DF4E
    else:
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
