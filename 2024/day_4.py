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

import os
import sys
# import typing  # pylint: disable=unused-import
# from typing import Optional  # pylint: disable=unused-import
# from typing import List  # pylint: disable=unused-import
# from typing import Tuple  # pylint: disable=unused-import


# xpylint: xdisable=import-error
from helpers.import_as_dataframe import import_as_dataframe
import helpers.day_4_count_matches
# pylint: enable=import-error

# Constants
__NAME__ = "day_4"  # this is us
__BASEDIR__ = f"{os.environ['HOME']}/Proj/adventofcode/2024"
__DATADIR__ = f"{__BASEDIR__}/data"  # data directory path

SEARCH_STRING = "XMAS"

def main(data_file: str, verbose=0):
    """main"""
    # Import data
    df = import_as_dataframe(data_file)
    # Search for target string and print results
    n_matches = helpers.day_4_count_matches.count_matches(df, SEARCH_STRING, verbose=1)
    print(f"Number of matches = {n_matches}")


# pylint: disable=invalid-name
if __name__ == "__main__":
    # Default data input
    input_file = f"{__DATADIR__}/{ __NAME__}_data_example"
    # Check for a commandline argument and use that as
    # the path to the file containing the input data
    try:
        input_file = sys.argv[1]
        if not os.access(input_file, os.R_OK):
            raise OSError
    except OSError as exception:
        raise SystemExit("No such file") from exception
    except IndexError:
        pass
    main(data_file=input_file)
