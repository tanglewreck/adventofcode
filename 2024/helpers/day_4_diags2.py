# coding: utf-8
"""
    get_diags

    author
        mier

    date
        2025-06-01
"""

import numpy as np
import pandas as pd

def upper_right_right_to_left(df: pd.DataFrame):
    """
        upper_right_right_to_left()

        returns
            diagonals starting at the upper-right corner
            and going down right-to-left
    """
    n = len(df)
    diags = []
    for r in range(n):
        diag = []
        col = n-2-r
        for row in range(0, n):
            diag.append(df.iloc[row, col])
            col -= 1
            if col < 0:
                break
        diags.append(diag)
    return diags


def upper_left_left_to_right(df: pd.DataFrame):
    """
        upper_right_right_to_left()

        returns
            diagonals starting at the upper-right corner
            and going down right-to-left
    """
    n = len(df)
    diags = []
    for r in range(n):
        diag = []
        col = r+1
        for row in range(n-1-r):
            diag.append(df.iloc[row, col])
            col += 1
        diags.append(diag)
    return diags


def lower_right_right_to_left(df: pd.DataFrame):
    """
        upper_right_right_to_left()

        returns
            diagonals starting at the upper-right corner
            and going down right-to-left
    """
    n = len(df)
    diags = []
    for r in range(n-1, -1, -1):
        diag = []
        col = n - 1
        for row in range(r, n):
            diag.append(df.iloc[row, col])
            col -= 1
        diags.append(diag)
    return diags


def lower_left_left_to_right(df: pd.DataFrame):
    """
        upper_right_right_to_left()

        returns
            diagonals starting at the upper-right corner
            and going down right-to-left
    """
    n = len(df)
    diags = []
    for r in range(n-1, -1, -1):
        diag = []
        col = 0
        for row in range(r, n):
            diag.append(df.iloc[row, col])
            col += 1
        diags.append(diag)
    return diags


def get_diags(df: pd.DataFrame):
    """
        get_diags()

        date
            2025-06-01
    """
    diags = []
    diags.extend(lower_left_left_to_right(df))
    diags.extend(upper_left_left_to_right(df))
    diags.extend(lower_right_right_to_left(df))
    diags.extend(upper_right_right_to_left(df))
    return diags


def count_xmas(df: pd.DataFrame) -> int:
    """
        count_xmas()

        count the number of times the string "XMAS" (or "SAMX") occurs
        on rows, columns, and diagonals in a dataframe df
    """
    # extract rows, columns, and diagonals
    df_rows = [list(row) for row in np.asarray(df)]
    df_cols = [list(row) for row in np.asarray(df).T]
    diags = get_diags(df)
    # turn them into lists of strings
    row_strings = ["".join(row) for row in df_rows]
    col_strings = ["".join(col) for col in df_cols]
    diag_strings = ["".join(diag) for diag in diags]
    # count the number of "XMAS" and "SAMX"
    n_rows = sum((r.count("XMAS") + r.count("SAMX") for r in row_strings))
    n_rows += sum((r.count("xmas") + r.count("samx") for r in row_strings))
    n_cols = sum((c.count("XMAS") + c.count("SAMX") for c in col_strings))
    n_cols += sum((c.count("xmas") + c.count("samx") for c in col_strings))
    n_diags = sum((d.count("XMAS") + d.count("SAMX") for d in diag_strings))
    n_diags += sum((d.count("xmas") + d.count("samx") for d in diag_strings))
    print(f"n_matches (rows) {n_rows}")
    print(f"n_matches (cols) {n_cols}")
    print(f"n_matches (diags) {n_diags}")
    return n_rows + n_cols + n_diags
