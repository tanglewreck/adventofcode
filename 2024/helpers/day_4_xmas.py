# coding: utf-8
"""
    day_4_xmas.py
"""
import pandas as pd
import numpy as np


__all__ = ["x_mas_list", "x_mas_pd", "x_mas_np"]


def x_mas_pd(df: pd.DataFrame):
    """
        Find X-MAS patterns, pandas version
    """
    n = len(df)
    count = 0
    for row in range(1, n - 1):
        for col in range(1, n - 1):
            if df.iloc[row, col] == 'A':
                # up-left and up-right
                ul, ur = (df.iloc[row - 1, col - 1], df.iloc[row - 1, col + 1])
                above = str(ul) + str(ur)
                # down-left and up-right
                dl, dr = (df.iloc[row + 1, col - 1], df.iloc[row + 1, col + 1])
                below = str(dl) + str(dr)
                # check for X-MAS patterns
                if above == "MM" and below == "SS":
                    count += 1
                if above == "MS" and below == "MS":
                    count += 1
                if above == "SM" and below == "SM":
                    count += 1
                if above == "SS" and below == "MM":
                    count += 1
    return count


def x_mas_np(df: pd.DataFrame):
    """
        Find X-MAS patterns, numpy version
    """
    rows = np.asarray(df)
    n = len(rows)
    count = 0
    for row in range(1, n - 1):
        for col in range(1, n - 1):
            if rows[row, col] == 'A':
                # up-left and up-right
                ul, ur = (rows[row - 1, col - 1], rows[row - 1, col + 1])
                above = ul + ur
                # down-left and up-right
                dl, dr = (rows[row + 1, col - 1], rows[row + 1, col + 1])
                below = dl + dr
                # check for X-MAS patterns
                if above == "MM" and below == "SS":
                    count += 1
                if above == "MS" and below == "MS":
                    count += 1
                if above == "SM" and below == "SM":
                    count += 1
                if above == "SS" and below == "MM":
                    count += 1
    return count


def x_mas_list(df: pd.DataFrame):
    """
        Find X-MAS patterns, list version
    """
    rows = [list(row) for row in np.asarray(df)]
    n = len(rows)
    count = 0
    for row in range(1, n - 1):
        for col in range(1, n - 1):
            if rows[row][col] == 'A':
                # up-left and up-right
                ul, ur = rows[row - 1][col - 1], rows[row - 1][col + 1]
                above = ul + ur
                # down-left and up-right
                dl, dr = rows[row + 1][col - 1], rows[row + 1][col + 1]
                below = dl + dr
                # check for X-MAS patterns
                if above == "MM" and below == "SS":
                    count += 1
                if above == "MS" and below == "MS":
                    count += 1
                if above == "SM" and below == "SM":
                    count += 1
                if above == "SS" and below == "MM":
                    count += 1
    return count
