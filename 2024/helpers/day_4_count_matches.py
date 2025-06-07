"""
    count_matches

"""

import re
# from typing import Optional  # pylint: disable=unused-import
# from typing import List  # pylint: disable=unused-import
# from typing import Tuple  # pylint: disable=unused-import

import pandas as pd
from . day_4_extract_diagonals import extract_diagonals

# Constants
SEARCH_STRING = "XMAS"


def count_matches(df: pd.DataFrame,
                  search_string: str = SEARCH_STRING,
                  verbose: int = 0) -> int:
    """
        Search for a string embedded in the row, columns, and diagonals
        of a dataframe using regular expressions (which enable case-
        insensitive searches, if that is what you want...)
    """
    n_rows = len(df)
    n_cols = len(df.iloc[0])
    if verbose > 0:
        print(f"n_rows = {n_rows}")
        print(f"n_cols = {n_cols}")
    if not search_string:
        search_string = "xmas"

    # Allow data to contain '_', '.', ',', ' ', and ignore them in the search
    r = re.compile(r'[_., ]*'.join(re.split('', search_string)[1:-1]), re.IGNORECASE)
    rr = re.compile(r'[_., ]*'.join(re.split('', search_string[::-1])[1:-1]), re.IGNORECASE)

    # Total number of hits
    n_matches_tot = 0

    # Search ROWS
    n_matches = 0
    for row in range(n_rows):
        row_str = "".join(df.iloc[row, 0:n_cols])
        matches = re.findall(r, row_str)
        matches_r = re.findall(rr, row_str)
        n_matches += len(matches)
        n_matches += len(matches_r)
        if (matches or matches_r) and verbose > 1:
            print(matches + matches_r)
            row_str = row_str.replace("_", "")
            print("count():", row_str.count("XMAS") + row_str.count("SAMX"))
            print("count():", row_str.count("xmas") + row_str.count("samx"))
    n_matches_tot += n_matches
    if verbose > 0:
        print(f"n_matches (rows) = {n_matches}")

    # Search COLUMNS
    n_matches = 0
    for col in range(n_cols):
        col_str = "".join(df.iloc[:, col])
        matches = re.findall(r, col_str)
        matches_r = re.findall(rr, col_str)
        n_matches += len(matches)
        n_matches += len(matches_r)
        if (matches or matches_r) and verbose > 1:
            print(f"column {col}: {col_str}")
            print(matches + matches_r)
            col_str = col_str.replace("_", "")
            print("count():", col_str.count("XMAS") + col_str.count("SAMX"))
            print("count():", col_str.count("xmas") + col_str.count("samx"))
    n_matches_tot += n_matches
    if verbose > 0:
        print(f"n_matches (cols) = {n_matches}")

    # Search DIAGONALS
    n_matches = 0
    for k, diag in enumerate(extract_diagonals(df)):
        diag_str = "".join(diag)
        matches = re.findall(r, diag_str)
        matches_r = re.findall(rr, diag_str)
        n_matches += len(matches)
        n_matches += len(matches_r)
        if (matches or matches_r) and verbose > 1:
            print(f"{k}: diag {diag}: {diag_str}")
            print(matches + matches_r)
            diag_str = diag_str.replace("_", "")
            print("count():", diag_str.count("XMAS") + diag_str.count("SAMX"))
            print("count():", diag_str.count("xmas") + diag_str.count("samx"))
        if verbose > 1:
            print(f"{k}: diag_str = {diag_str}")
    n_matches_tot += n_matches
    if verbose > 0:
        print(f"n_matches (diags) = {n_matches}")
    # Return number of matches
    return n_matches_tot
