"""

    --- Day 4: Ceres Search ---

    "Looks like the Chief's not here. Next!" One of The Historians pulls out a
    device and pushes the only button on it. After a brief flash, you recognize
    the interior of the Ceres monitoring station!

    As the search for the Chief continues, a small Elf who lives on the station
    tugs on your shirt; she'd like to know if you could help her with her word
    search (your puzzle input). She only has to find one word: XMAS.

    This word search allows words to be
    - horizontal
    - vertical
    - diagonal
    - written backwards
    - even overlapping other words

    It's a little unusual, though, as you don't merely need to find one
    instance of XMAS - you need to find all of them.

    Here are a few ways XMAS might appear, where irrelevant characters have
    been replaced with .:

        ..X...
        .SAMX.
        .A..A.
        XMAS.S
        .X....__

    The actual word search will be full of letters instead. For example:

    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX

    In this word search, XMAS occurs a total of 18 times; here's the
    same word search again, but where letters not involved in any XMAS
    have been replaced with .:

        -------------------
        0 1 2 3 4 5 6 7 8 9
        -------------------
    0   . . . . X X M A S .
    1   . S A M X M S . . .
    2   . . . S . . A . . .
    3   . . A . A . M S . X
    4   X M A S A M X . M M
    5   X . . . . . X A . A
    6   S . S . S . S . S S
    7   . A . A . A . A . A
    8   . . M . M . M . M M
    9   . X . X . X M A S X

    Take a look at the little Elf's word search.
    How many times does XMAS appear?



"""


# xpylint: disable=too-many-locals
# xpylint: disable=too-many-statements
# xpylint: disable=unused-argument
# xpylint: disable=unused-import
# xpylint: disable=unused-variable
# xpylint: disable=undefined-variable


import re
import typing
from typing import Optional
from typing import List
from typing import Tuple
import numpy as np
import pandas as pd

# TEST_DATA = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# """

FULL_DATA_CSV = "data/day_4_data.csv"
EXAMPLE_DATA_CSV = "data/day_4_data_example.csv"


@typing.no_type_check
def import_data(path: str, verbose: int = 0) -> Tuple[str, str]:
    """Read data from file"""
    try:
        if verbose > 0:
            print(f"path = {path}")
        with open(path + "_example", encoding="utf-8") as fp:
            example_data = fp.read().strip()
        with open(path, encoding="utf-8") as fp:
            full_data = fp.read().strip()
        return (example_data, full_data)
# pylint: enable=unused-variable
    except OSError as exception:
        print(repr(exception))
        raise SystemExit(1) from exception


@typing.no_type_check
def import_as_dataframe(path: str, verbose: int = 0) -> Optional[pd.DataFrame]:
    """import and save as csv"""
    outpath = path + ".csv"
    if verbose > 0:
        print(outpath)
    try:
        with open(path, encoding="utf-8") as fp:
            rows = [re.split(r'', row.strip())[1:-1] for row in fp.readlines()]
            if verbose:
                print(f"rows: {rows}")
            # rows = [",".join(
            #    (re.split(r'', row.strip()))[1:-1]) + "\n"
            #        for row in fp.readlines()
            # ]
            if verbose > 0:
                print(f"Rows read: {rows}")
            return pd.DataFrame(rows)
            # with open(outpath, "w", encoding="utf-8") as fp_out:
            #    fp_out.writelines(rows)
            # return pd.DataFrame()
    except OSError as exception:
        print(repr(exception))
        return None
        # raise SystemExit(1) from exception
    return None


def diagonals(df_in: pd.DataFrame, verbose: int = 0) -> List[str]:
    """Extract diagonals from a dataframe"""
    # Convert to np.ndarray so that we can use
    # np.diagonal() to extract diagonals (make
    # a copy so the input dataframe is not affected).
    df = np.asarray(df_in.copy())
    # Flip data left-to-right, i.e. reverse/mirror rows
    df_flipped = np.fliplr(df)
    n = len(df)
    diags: list = [df[row_col:n, :(n - row_col)].diagonal()
                   for row_col in range(n)]
    diags_flipped: list = [df_flipped[row_col:n, :(n - row_col)].diagonal()
                           for row_col in range(n)]
    if verbose > 1:
        print(f"diagonals: {diags}")
        print(f"diagonals (flipped df): {diags_flipped}")
    return diags + diags_flipped


# pylint: disable=too-many-locals
def search_and_extract(df: pd.DataFrame, search_string: str,
                       verbose: int = 0) -> int:
    """
        Search for a string embedded in the row, columns, and diagonals
        of a dataframe
    """
    # n_string_in_rows = [search_string in df[]]
    regexp = re.compile(rf"{search_string}")
    n = len(df)
    n_matches = 0
    # Search rows
    n_row_matches = 0
    for row in range(n):
        row_str = "".join(df.iloc[row])
        row_str_rev = "".join(df.iloc[row])[::-1]
        n_row_matches += len(re.findall(regexp, row_str))
        n_row_matches += len(re.findall(regexp, row_str_rev))
    if verbose:
        print(f"n_row_matches = {n_row_matches}")
    n_matches += n_row_matches
    # Search columns
    n_col_matches = 0
    for col in range(n):
        col_str = "".join(df.iloc[:, col])
        col_str_rev = "".join(df.iloc[:, col])[::-1]
        n_col_matches += len(re.findall(regexp, col_str))
        n_col_matches += len(re.findall(regexp, col_str_rev))
    if verbose:
        print(f"n_col_matches = {n_col_matches}")
    n_matches += n_col_matches
    # Search diagonals
    n_diag_matches = 0
    diags = diagonals(df)
    for diag in diags:
        diag_str = "".join(diag)
        diag_str_rev = "".join(diag[::-1])
        if verbose > 1:
            print(f"diag_str = {diag_str}")
            print(f"diag_str_rev = {diag_str_rev}")
        n_diag_matches += len(re.findall(regexp, diag_str))
        n_diag_matches += len(re.findall(regexp, diag_str_rev))
    if verbose:
        print(f"n_diag_matches = {n_diag_matches}")
    n_matches += n_diag_matches
    # Print diagnostics if verbose enogugh
    if verbose > 1:
        print(f"Diagonals = {diags}")
    if verbose > 1:
        print(n_matches)
    # Return number of matches
    return n_matches


def main(verbose=0):
    """main"""
    # Import data
    # example_data, full_data = import_data("../data/day_4_data")
    df_example = import_as_dataframe("data/day_4_data_example")
    if verbose > 0:
        print(df_example)
        print()
    df_full = import_as_dataframe("data/day_4_data")
    # Search for target string and print results
    target_string = 'XMAS'
    print("Number of matches (example data))= "
          f"{search_and_extract(df_example, target_string, verbose=1)}")
    print("Number of matches (full data))= "
          f"{search_and_extract(df_full, target_string, verbose=1)}")


if __name__ == "__main__":
    main(verbose=0)
