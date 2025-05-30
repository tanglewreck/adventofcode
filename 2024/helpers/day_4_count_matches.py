"""
    count_matches

"""
# xpylint: disable=too-many-locals
# xpylint: disable=too-many-statements
# xpylint: disable=unused-argument
# xpylint: disable=unused-import
# pylint: disable=unused-variable
# xpylint: disable=undefined-variable

import re
import typing  # pylint: disable=unused-import
from typing import Optional  # pylint: disable=unused-import
from typing import List  # pylint: disable=unused-import
from typing import Tuple  # pylint: disable=unused-import
import numpy as np  # pylint: disable=unused-import
import pandas as pd
from . day_4_diags import extract_diagonals

# Constants
SEARCH_STRING = "XMAS"

def count_matches(df: pd.DataFrame,
                       search_string: str = SEARCH_STRING,
                       verbose: int = 0) -> int:
    """
        Search for a string embedded in the row, columns, and diagonals
        of a dataframe
    """
    n = len(df)
    regexp = re.compile(rf"{search_string}")
    regexp_rev = re.compile(rf"{search_string[::-1]}")
    # Total number of hits
    n_matches_tot = 0
    # Search rows
    n_matches = 0
    for row in range(n):
        row_str = "".join(df.iloc[row])
        n_matches += len(re.findall(regexp, row_str))
        n_matches += len(re.findall(regexp_rev, row_str))
    n_matches_tot += n_matches
    if verbose:
        print(f"n_matches (rows) = {n_matches}")
    # Search columns
    n_matches = 0
    for col in range(n):
        col_str = "".join(df.iloc[:, col])
        matches = re.findall(regexp, col_str)
        matches_rev = re.findall(regexp_rev, col_str)
        if matches and verbose > 1:
            print(f"column {col}: ", end="")
            print(matches)
        if matches_rev and verbose > 1:
            print(f"column {col}: ", end="")
            print(matches_rev)
        n_matches += len(re.findall(regexp, col_str))
        n_matches += len(re.findall(regexp_rev, col_str))
    n_matches_tot += n_matches
    if verbose:
        print(f"n_matches (cols) = {n_matches}")
    # Search diagonals
    n_matches = 0
    for k, diag in enumerate(extract_diagonals(df)):
        diag_str = "".join(diag)
        diag_str_rev = "".join(diag[::-1])
        if verbose > 1:
            print(f"diag_str = {diag_str}")
            print(f"diag_str_rev = {diag_str_rev}")
        matches = re.findall(regexp, diag_str)
        matches_rev = re.findall(regexp_rev, diag_str)
        if matches and verbose > 1:
            print(f"diag {k}: {diag}: ", end="")
            print(matches)
        if matches_rev and verbose > 1:
            print(f"diag {k}: {diag}: ", end="")
            print(matches_rev)
        n_matches += len(re.findall(regexp, diag_str))
        n_matches += len(re.findall(regexp, diag_str_rev))
    n_matches_tot += n_matches
    if verbose:
        print(f"n_matches (diags) = {n_matches}")
    # Return number of matches
    return n_matches_tot
