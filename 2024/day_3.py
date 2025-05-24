"""
    --- Day 3: Mull It Over ---

    "Our computers are having issues, so I have no idea if we have any Chief
    Historians in stock! You're welcome to check the warehouse, though," says the
    mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The
    Historians head out to take a look.

    The shopkeeper turns to you. "Any chance you can see why our computers are
    having issues again?"

    The computer appears to be trying to run a program, but its memory (your
    puzzle input) is corrupted. All of the instructions have been jumbled up!

    It seems like the goal of the program is just to multiply some numbers. It
    does that with instructions like mul(X,Y), where X and Y are each 1-3 digit
    numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024.
    Similarly, mul(123,4) would multiply 123 by 4.

    However, because the program's memory has been corrupted, there are also
    many invalid characters that should be ignored, even if they look like part of
    a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 )
    do nothing.

    For example, consider the following section of corrupted memory:

        xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

    Only the four highlighted sections are real mul instructions. Adding up the
    result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

    Scan the corrupted memory for uncorrupted mul instructions. What do you get
    if you add up all of the results of the multiplications?

    ------------------------------------------------------------
    Your puzzle answer was 188192787.
    The first half of this puzzle is complete! It provides one gold star: *
    ------------------------------------------------------------


    --- Part Two ---

    As you scan through the corrupted memory, you notice that some of the
    conditional statements are also still intact. If you handle some of the
    uncorrupted conditional statements in the program, you might be able to get an
    even more accurate result.

    There are two new instructions you'll need to handle:

        - The do() instruction enables future mul instructions.
        - The don't() instruction disables future mul instructions.

    Only the most recent do() or don't() instruction applies. At the beginning of
    the program, mul instructions are enabled.

    For example:

    xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

    This corrupted memory is similar to the example from before, but this time the
    mul(5,5) and mul(11,8) instructions are disabled because there is a don't()
    instruction before them. The other mul instructions function normally,
    including the one at the end that gets re-enabled by a do() instruction.

    This time, the sum of the results is 48 (2*4 + 8*5).

    Handle the new instructions; what do you get if you add up all of the results
    of just the enabled multiplications?

"""


# pylint: disable=unused-import
# import numpy as np
# import pandas as pd
# pylint: enable=unused-import
# import re
from string import digits


# def mul(x: int|float, y: int|float) -> int | float:
#     """Multiply two numbers"""
#     return x * y
#
#
# def day_3_part_1() -> None:
#     """day_3_part_1()"""
#     fdata = "data/day_3_data"
#     fdata_example = "data/day_3_data_example"
#     # Import data
#     try:
#         with open(fdata_example, encoding="utf-8") as fp:
#             data_example = fp.read()
#         with open(fdata, encoding="utf-8") as fp:
#             data= fp.read()
#     except OSError as exception:
#         print(repr(exception))
#         raise SystemExit(1) from exception
#     # Compile a regexp that will match 'mul(<num>,<num>)'
#     mul_regexp = re.compile(r"mul\(\d+,\s*\d+\)")
#     # Prepare two lists that will hold the reults of
#     # the multiplications
#     mul_results, mul_results_example = [], []
#     # Get results for the example-data
#     for match in mul_regexp.findall(data_example):
#         # pylint: disable=eval-used
#         mul_results_example.append(eval(match))
#     # Get results for the full data
#     for match in mul_regexp.findall(data):
#         # pylint: disable=eval-used
#         mul_results.append(eval(match))
#     # Print results
#     print(f"Sum of multiplications (example data)= {sum(mul_results_example)}")
#     print(f"Sum of multiplications (full data) = {sum(mul_results)}")
#
#

# TEST_DATA = "xyxmul(123,456)xyzmuöl(38),.mul(1,2)mul(3,3333)sjsjX"
TEST_DATA = "xyxmul(100,456)xyzmuöl(38),.mul(1,2)mul(3,10)sjsjX"
TEST_DATA_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


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

# pylint: disable=too-many-branches
def parse_data(data: str = TEST_DATA, do_dont: bool = False,
               verbose: int = 0) -> list:
    """
        parse_data()
            Extracts valid tokens (substrings of the form 'mul(x,y)', where x and y
            are integers) from a string.

            Returns a list of token-strings.
    """
    valid_tokens = []  # A list that will hold valid tokens ('mul(x,y)'-substrings)
    valid = True  # Indicator that a token is (still) valid
    eof = False  # flag that indicates whether we have reached end-of-file (end-of-data)
    index = 0  # index into to the data
    # do_token_length = 4  # length of a 'do()' token
    # dont_token_length = 7  # length of a "don't()" token
    do = True
    while valid and not eof:
        try:
            # Check for 'do()' and "don't()"tokens
            if get_token(data, index, 4) == "do()":
                if verbose > 0:
                    print("found a 'do()' token")
                do = True
            if get_token(data, index, 7) == "don't()":
                if verbose > 0:
                    print("found a 'don't()' token")
                do = False
            # Set token-length
            token_length = 4
            # Check that we do not go beoynd the length of the data
            if index + token_length > len(data):
                eof = True
                continue
            # Get next token
            token = get_token(data, index, token_length)
            # If token does not match the beginning of a 'mul(x,y)' operation
            # move one step forward and start the while-loop over
            if token != "mul(":
                index += 1
                continue
            # Increase token-length by 1
            token_length += 1
            # Loop while the token ends in a digit
            while get_token(data, index, token_length)[-1] in digits:
                token = get_token(data, index, token_length)
                token_length += 1
            # If the token now ends with a ",", update the token
            # and investigate further
            if get_token(data, index, token_length)[-1] == ",":
                token = get_token(data, index, token_length)
                token_length += 1
                # Again, if the token ends with a digit, increase token-length
                # by one, update the token, and and repeat until the token
                # does not end with a digit
                while get_token(data, index, token_length)[-1] in digits:
                    token = get_token(data, index, token_length)
                    token_length += 1
                # Token now ends with a non-digit. If it ends with a ")",
                # we have found a valid token, so we add it to the list of
                # valid tokens, but only if the lastest do()/don't() token
                # was a 'do()'.
                if get_token(data, index, token_length)[-1] == ")":
                    token = get_token(data, index, token_length)
                    if do or not do_dont:
                        valid_tokens.append(token)
                    token_length += 1
                    if verbose > 0:
                        print(token)
            index += len(token)
        except IndexError:
            pass
    if verbose > 0:
        print(valid_tokens)
    return valid_tokens


def main() -> None:
    """main()"""
# pylint: disable=unused-variable
    # Import data
    fdata = "data/day_3_data"
    fdata_example = "data/day_3_data_example"
    fdata_example_2 = "data/day_3_data_example_part_2"
    try:
        with open(fdata_example, encoding="utf-8") as fp:
            example_data = fp.read()
        with open(fdata_example_2, encoding="utf-8") as fp:
            example_data_2 = fp.read()
        with open(fdata, encoding="utf-8") as fp:
            full_data= fp.read()
        data = full_data
# pylint: enable=unused-variable
    except OSError as exception:
        print(repr(exception))
        raise SystemExit(1) from exception

    # Get tokens
    tokens = parse_data(data, do_dont=False, verbose=0)
    token_sum = 0
    # pylint: disable=eval-used
    for token in tokens:
        token_sum += eval(token)
    print("do/dont = False")
    print(f"Sum of mul()-tokens = {token_sum}")
    print(f"Number of mul()-tokens = {len(tokens)}")
    print()


    # Get tokens
    tokens = parse_data(data, do_dont=True, verbose=0)
    token_sum = 0
    # pylint: disable=eval-used
    for token in tokens:
        token_sum += eval(token)
    print("do/dont = True")
    print(f"Sum of mul()-tokens = {token_sum}")
    print(f"Number of mul()-tokens = {len(tokens)}")

if __name__ == "__main__":
    main()
