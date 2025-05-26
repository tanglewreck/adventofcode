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


# pylint: disable=unused-import
# import numpy as np
# import pandas as pd
import re
from string import digits
from typing import Callable, List, Optional, Tuple
# pylint: enable=unused-import


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


def mul(x: int|float, y: int|float) -> int|float:
    """Multiply two numbers"""
    return x * y


def get_token(data_string: str, index: int, length: int) -> str:
    """
        get_token()
            Return a substring of length 'length' beginning at 'index'.
    """
    try:
        return data_string[index : index + length]
    except IndexError:
        return ""


def import_data(path: str, verbose: int = 0) -> Tuple[str, str]:
    """Read data from file"""
    try:
        if verbose > 0:
            print(f"path = {path}")
        with open(path + "_example", encoding="utf-8") as fp:
            example_data = fp.read().strip()
        with open(path, encoding="utf-8") as fp:
            full_data= fp.read().strip()
        return (example_data, full_data)
# pylint: enable=unused-variable
    except OSError as exception:
        print(repr(exception))
        raise SystemExit(1) from exception


def parse_data(data, verbose=0):
    """
        parse_data()

    """
    return data, verbose


def main() -> None:
    """main()"""
# pylint: disable=unused-variable
    # Import data
    fdata = "data/day_4_data"
    fdata_example = "data/day_4_data_example"
    example_data, full_data = import_data(fdata)

    print(full_data)
    print()
    print(example_data)

    # Get tokens
    tokens = parse_data(example_data, verbose=0)
    ntokens = len(tokens)
    # pylint: disable=eval-used
    print(f"Number of tokens = {ntokens}")
    print()


if __name__ == "__main__":
    main()
#
#
# pylint: disable=too-many-branches
# def parse_data(data: str = TEST_DATA, do_dont: bool = False,
#                verbose: int = 0) -> list:
#     """
#         parse_data()
#             Extracts valid tokens (substrings of the form 'mul(x,y)', where x and y
#             are integers) from a string.
#
#             Returns a list of token-strings.
#     """
#     valid_tokens = []  # A list that will hold valid tokens ('mul(x,y)'-substrings)
#     valid = True  # Indicator that a token is (still) valid
#     eof = False  # flag that indicates whether we have reached end-of-file (end-of-data)
#     index = 0  # index into to the data
#     # do_token_length = 4  # length of a 'do()' token
#     # dont_token_length = 7  # length of a "don't()" token
#     do = True
#     while valid and not eof:
#         try:
#             # Check for 'do()' and "don't()"tokens
#             if get_token(data, index, 4) == "do()":
#                 if verbose > 0:
#                     print("found a 'do()' token")
#                 do = True
#             if get_token(data, index, 7) == "don't()":
#                 if verbose > 0:
#                     print("found a 'don't()' token")
#                 do = False
#             # Set token-length
#             token_length = 4
#             # Check that we do not go beoynd the length of the data
#             if index + token_length > len(data):
#                 eof = True
#                 continue
#             # Get next token
#             token = get_token(data, index, token_length)
#             # If token does not match the beginning of a 'mul(x,y)' operation
#             # move one step forward and start the while-loop over
#             if token != "mul(":
#                 index += 1
#                 continue
#             # Increase token-length by 1
#             token_length += 1
#             # Loop while the token ends in a digit
#             while get_token(data, index, token_length)[-1] in digits:
#                 token = get_token(data, index, token_length)
#                 token_length += 1
#             # If the token now ends with a ",", update the token
#             # and investigate further
#             if get_token(data, index, token_length)[-1] == ",":
#                 token = get_token(data, index, token_length)
#                 token_length += 1
#                 # Again, if the token ends with a digit, increase token-length
#                 # by one, update the token, and and repeat until the token
#                 # does not end with a digit
#                 while get_token(data, index, token_length)[-1] in digits:
#                     token = get_token(data, index, token_length)
#                     token_length += 1
#                 # Token now ends with a non-digit. If it ends with a ")",
#                 # we have found a valid token, so we add it to the list of
#                 # valid tokens, but only if the lastest do()/don't() token
#                 # was a 'do()'.
#                 if get_token(data, index, token_length)[-1] == ")":
#                     token = get_token(data, index, token_length)
#                     if do or not do_dont:
#                         valid_tokens.append(token)
#                     token_length += 1
#                     if verbose > 0:
#                         print(token)
#             index += len(token)
#         except IndexError:
#             pass
#     if verbose > 0:
#         print(valid_tokens)
#     return valid_tokens
