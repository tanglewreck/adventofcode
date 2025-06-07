#!/usr/bin/env python
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

        --> 2549 <--

    Your puzzle answer was 2549.

    The first half of this puzzle is complete! It provides one gold star: *

    --- Part Two ---

    The Elf looks quizzically at you. Did you misunderstand the assignment?

    Looking for the instructions, you flip over the word search to find that
    this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're
    supposed to find two MAS in the shape of an X. One way to achieve that is
    like this:

    M.S
    .A.
    M.S

    Irrelevant characters have again been replaced with . in the above diagram.
    Within the X, each MAS can be written forwards or backwards.

    Here's the same example from before, but this time all of the X-MASes have
    been kept instead:

    .M.S......
    ..A..MSMS.
    .M.S.MAA..
    ..A.ASMSM.
    .M.S.M....
    ..........
    S.S.S.S.S.
    .A.A.A.A..
    M.M.M.M.M.
    ..........

    In this example, an X-MAS appears 9 times.

    Flip the word search from the instructions back over to the word search
    side and try again. How many times does an X-MAS appear?

        --> 2003 <--

    That's the right answer! You are one gold star closer to finding the Chief
    Historian.

"""
import argparse
import time
from pathlib import Path
from helpers import count_matches
from helpers import count_xmas
from helpers import x_mas_list, x_mas_pd, x_mas_np
from utils import as_dataframe
from utils import get_data_path
from utils import verbose_msg

__version__ = "2025.06.07_01"
__author__ = "mier"

# this determines which data files are read
__DAYNUM__ = 4  # this is day 4

# shis is the string we're looking for
SEARCH_STRING = "xmas"


def part_1(example: bool = False, verbose: int = 0, time_it: bool = False):
    """
        part_1()
    """
    # get data
    part = 1
    data_path: Path = get_data_path(__DAYNUM__, part=part, example=example)
    df = as_dataframe(data_path, save=False)
    verbose_msg(f"{df}", 2, verbose)
    # ...
    # Search for target string and print results
    pre = time.time()
    n_matches = count_matches(df, SEARCH_STRING, verbose=verbose)
    post = time.time()
    print(f"matches = {n_matches} (count_matches, using regexps)")
    if time_it:
        print(f"elapsed = {post - pre:.4f}s")

    pre = time.time()
    n_matches = count_xmas(df)
    post = time.time()
    print(f"matches = {n_matches} (count_xmas)")
    if time_it:
        print(f"elapsed = {post - pre:.4f}s")


def part_2(example: bool = False, verbose: int = 0, time_it: bool = False):
    """part_2()"""
    # get data
    part = 2
    data_path: Path = get_data_path(__DAYNUM__, part=part, example=example)
    df = as_dataframe(data_path, save=False)
    verbose_msg(f"{df}", 2, verbose)

    # x_mas_list()
    pre = time.time()
    print("lists:", x_mas_list(df))
    post = time.time()
    if time_it:
        print(f"elapsed = {post - pre:.4f}s")

    # x_mas_np()
    pre = time.time()
    print("numpy:", x_mas_np(df))
    post = time.time()
    if time_it:
        print(f"elapsed = {post - pre:.4f}s")

    # x_mas_pd()
    pre = time.time()
    print("pandas:", x_mas_pd(df))
    post = time.time()
    if time_it:
        print(f"elapsed = {post - pre:.4f}s")


def main():
    """main()"""
    parser = argparse.ArgumentParser(description=f"aoc 2024 day {__DAYNUM__}",
                                     prog=f"day_{__DAYNUM__}",
                                     add_help=True)
    parser.add_argument('--part', type=int, default=1,
                        choices=[1, 2],
                        help='part number (1 or 2)')
    parser.add_argument('--example', default=False,
                        action='store_true',
                        help='use example datafile')
    parser.add_argument('--time', default=False,
                        action='store_true',
                        help='time it')
    parser.add_argument('--verbose', type=int, default=0,
                        choices=[0, 1, 2],
                        help='get diagnostics')
    args = parser.parse_args()
    if args.part == 1:
        part_1(args.example, args.verbose, args.time)
    else:
        part_2(args.example, args.verbose, args.time)


if __name__ == "__main__":
    main()
# vim: set numberwidth=4 number noignorecase :
