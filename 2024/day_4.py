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

    M  M  M  S  X  X  M  A  S  M
    M  S  A  M  X  M  S  M  S  A
    A  M  X  S  X  M  A  A  M  M
    M  S  A  M  A  S  M  S  M  X
    X  M  A  S  A  M  X  A  M  M
    X  X  A  M  M  X  X  A  M  A
    S  M  S  M  S  A  S  X  S  S
    S  A  X  A  M  A  S  A  A  A
    M  A  M  M  M  X  M  M  M  M
    M  X  M  X  A  X  M  A  S  X

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
# pylint: disable=unused-variable
# xpylint: disable=undefined-variable

import re
import typing  # pylint: disable=unused-import
from typing import Optional  # pylint: disable=unused-import
from typing import List  # pylint: disable=unused-import
from typing import Tuple  # pylint: disable=unused-import
import numpy as np  # pylint: disable=unused-import
import pandas as pd

from snippets.import_as_dataframe import import_as_dataframe
from snippets.day_4_4_diags import extract_diagonals

FULL_DATA = "data/day_4_data"
FULL_DATA_CSV = "data/day_4_data.csv"
EXAMPLE_DATA = "data/day_4_data_example"
EXAMPLE_DATA_CSV = "data/day_4_data_example.csv"


# pylint: disable=too-many-branches
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
def search_and_extract(df: pd.DataFrame, search_string: str,
                       verbose: int = 0) -> int:
    """
        Search for a string embedded in the row, columns, and diagonals
        of a dataframe
    """
    search_string_rev = search_string[::-1]
    # n_string_in_rows = [search_string in df[]]
    regexp = re.compile(rf"{search_string}")
    regexp_rev = re.compile(rf"{search_string_rev}")
    n = len(df)
    n_matches = 0
    # Search rows
    n_row_matches = 0
    for row in range(n):
        row_str = "".join(df.iloc[row])
        row_str_rev = "".join(df.iloc[row])[::-1]
        n_row_matches += len(re.findall(regexp, row_str))
        n_row_matches += len(re.findall(regexp_rev, row_str))
    if verbose:
        print(f"n_row_matches = {n_row_matches}")
    n_matches += n_row_matches
    # Search columns
    n_col_matches = 0
    for col in range(n):
        col_str = "".join(df.iloc[:, col])
        col_str_rev = "".join(df.iloc[:, col])[::-1]
        matches = re.findall(regexp, col_str)
        matches_rev = re.findall(regexp_rev, col_str)
        if matches and verbose:
            print(f"column {col}: ", end="")
            print(matches)
        if matches_rev and verbose:
            print(f"column {col}: ", end="")
            print(matches_rev)
        n_col_matches += len(re.findall(regexp, col_str))
        n_col_matches += len(re.findall(regexp, col_str_rev))
    if verbose:
        print(f"n_col_matches = {n_col_matches}")
    n_matches += n_col_matches
    # Search diagonals
    n_diag_matches = 0
    # diags = diagonals(df)
    diags = extract_diagonals(df)
    for k, diag in enumerate(diags):
        diag_str = "".join(diag)
        diag_str_rev = "".join(diag[::-1])
        if verbose > 1:
            print(f"diag_str = {diag_str}")
            print(f"diag_str_rev = {diag_str_rev}")
        matches = re.findall(regexp, diag_str)
        matches_rev = re.findall(regexp_rev, diag_str)
        if matches and verbose:
            print(f"diag {k}: {diag}: ", end="")
            print(matches)
        if matches_rev and verbose:
            print(f"diag {k}: {diag}: ", end="")
            print(matches_rev)
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


# pylint: disable=unused-variable
def main(verbose=0):
    """main"""
    # Import data
    # example_data, full_data = import_data("../data/day_4_data")
    df_example = import_as_dataframe("data/day_4_data_example_3", save=True)
    if verbose > 0:
        print(df_example)
        print()
    df_full = import_as_dataframe("data/day_4_data_2", save=True)
    # Search for target string and print results
    target_string = 'XMAS'
    print("Number of matches (example data)= "
          f"{search_and_extract(df_example, target_string, verbose=0)}")
    print("Number of matches (full data)= "
          f"{search_and_extract(df_full, target_string, verbose=0)}")
    df_full = pd.read_csv("data/day_4_data_2.csv", header=None)
    df_example = pd.read_csv("data/day_4_data_example_3.csv", header=None)
    print("Number of matches (example data)= "
          f"{search_and_extract(df_example, target_string, verbose=0)}")
    print("Number of matches (full data)= "
          f"{search_and_extract(df_full, target_string, verbose=0)}")


if __name__ == "__main__":
    main()
