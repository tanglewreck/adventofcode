"""
    --- Day 3: Mull It Over ---

    "Our computers are having issues, so I have no idea if we have any Chief
    Historians in stock! You're welcome to check the warehouse, though," says
    the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The
    Historians head out to take a look.

    The shopkeeper turns to you. "Any chance you can see why our computers are
    having issues again?"

    The computer appears to be trying to run a program, but its memory (your
    puzzle input) is corrupted. All of the instructions have been jumbled up!

    It seems like the goal of the program is just to multiply some numbers. It
    does that with instructions like mul(X,Y), where X and Y are each 1-3 digit
    numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of
    2024.  Similarly, mul(123,4) would multiply 123 by 4.

    However, because the program's memory has been corrupted, there are also
    many invalid characters that should be ignored, even if they look like part
    of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or
    mul ( 2 , 4 ) do nothing.

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
    uncorrupted conditional statements in the program, you might be able to get
    an even more accurate result.

    There are two new instructions you'll need to handle:

        - The do() instruction enables future mul instructions.
        - The don't() instruction disables future mul instructions.

    Only the most recent do() or don't() instruction applies. At the beginning
    of the program, mul instructions are enabled.

    For example:

    xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

    This corrupted memory is similar to the example from before, but this time
    the mul(5,5) and mul(11,8) instructions are disabled because there is a
    don't() instruction before them. The other mul instructions function
    normally, including the one at the end that gets re-enabled by a do()
    instruction.

    This time, the sum of the results is 48 (2*4 + 8*5).

    Handle the new instructions; what do you get if you add up all of the
    results of just the enabled multiplications?

    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    A: 113965544
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    That's the right answer! You are one gold star closer to finding the Chief
    Historian.

    You have completed Day 3!


"""


import argparse
import time
from string import digits
# from utils import get_data_path
from utils.data_handler import DataHandler as dh
from utils.verbose_msg import verbose_msg


__DAYNUM__ = 3

# TEST_DATA = "xyxmul(123,456)xyzmuöl(38),.mul(1,2)mul(3,3333)sjsjX"
# TEST_DATA_2 = "xyxmul(100,456)xyzmuöl(38),.mul(1,2)mul(3,10)sjsjX"
# TEST_DATA_3 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def mul(x: int | float, y: int | float) -> int | float:
    """Multiply two numbers"""
    return x * y


def get_token(data_string: str, index: int, length: int) -> str:
    """
        get_token()
            Return a substring of length 'length' beginning at 'index'.
    """
    try:
        return data_string[index: index + length]
    except IndexError:
        return ""


def parse_data(data: str, do_dont: bool = False, verbose: int = 0) -> list:
    """
        parse_data()
            Extracts valid tokens (substrings of the form 'mul(x,y)', where x
            and y are integers) from a string.

            Returns a list of token-strings.

            NOTE: this could be done way much easier by using regexps... >:-^
    """
    valid_tokens = []  # A list that will hold valid tokens ('mul(x,y)'-substrings)
    index = 0  # index into to the data
    do_token_length = 4  # length of a 'do()' token
    dont_token_length = 7  # length of a "don't()" token
    do = True  # need to set this so we can test it further down
    while True:
        try:
            # Check for 'do()' and "don't()"tokens
            if get_token(data, index, do_token_length) == "do()":
                verbose_msg("found a 'do()' token", 2, verbose)
                do = True
            if get_token(data, index, dont_token_length) == "don't()":
                verbose_msg("found a 'don't()' token", 2, verbose)
                do = False
            # Set token-length ("mul(")
            token_length = 4
            # Check that we do not go beoynd the length of the data
            if index + token_length > len(data):
                break
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
                    verbose_msg(str(token), 3, verbose)
            index += len(token)
        except IndexError:
            print("SHOULDN'T GET HERE!")
    verbose_msg(str(valid_tokens), 3, verbose)
    return valid_tokens


def part_1_2(part: int = 1, example: bool = False, verbose: int = 0) -> int | None:
    """part_1_2()"""
    # Import data
    try:
        data = str(dh.import_data(day=__DAYNUM__, part=part, example=example, raw=True, dtype="str"))
    except OSError as exception:
        print(repr(exception))
        return None
    # Get tokens
    if part == 1:
        # part 1
        tokens = parse_data(data, do_dont=False, verbose=verbose)
    else:
        # part 2
        tokens = parse_data(data, do_dont=True, verbose=verbose)
    token_sum = 0
    # pylint: disable=eval-used
    for token in tokens:
        token_sum += eval(token)
    verbose_msg(f"number of tokens = {len(tokens)}", 1, verbose)
    # verbose_msg(f"sum of tokens = {token_sum}", 1, verbose)
    return token_sum


# def part_2(example: bool = False, verbose: int = 0) -> int | None:
#     """part_2() -- just a wrapper"""
#     part = 2
#     # Import data
#     # NB same full data as for part 1
#     try:
#         data = str(dh.import_data(day=__DAYNUM__, part=part, example=example, raw=True, dtype="str"))
#     except OSError as exception:
#         print(repr(exception))
#         return None
#     verbose_msg("part 2", 1, verbose)
#     # Get tokens
#     tokens = parse_data(data, do_dont=True, verbose=verbose)
#     token_sum = 0
#     # pylint: disable=eval-used
#     for token in tokens:
#         token_sum += eval(token)
#     verbose_msg(f"number of tokens = {len(tokens)}", 1, verbose)
#     # verbose_msg(f"sum of tokens = {token_sum}", 1, verbose)
#     return token_sum


def main():
    """main"""
    parser = argparse.ArgumentParser(description=f"aoc 2024 day {__DAYNUM__}",
                                     prog=f"day_{__DAYNUM__}",
                                     add_help=True)
    parser.add_argument('--part', type=int, default=1,
                        choices=[1, 2],
                        help='part number (1 or 2)')
    parser.add_argument('--time', default=False,
                        action='store_true',
                        help='time it')
    parser.add_argument('--example', default=False,
                        action='store_true',
                        help='use example datafile')
    parser.add_argument('--input', type=argparse.FileType('r'),
                        help='not used')
    parser.add_argument('--verbose', type=int, default=0,
                        choices=[0, 1, 2],
                        help='get diagnostics')
    args = parser.parse_args()
    pre = time.time()
    token_sum = part_1_2(args.part, args.example, args.verbose)
    post = time.time()
    if args.time:
        print(f"token_sum = {token_sum}", end="\t")
        print(f"({(post - pre):.4f}s)")
    else:
        print(f"token_sum = {token_sum}")


if __name__ == "__main__":
    main()
