# coding: utf-8
"""parser..."""

from string import digits

TEST_DATA = "xyxmul(123,456)xyzmuöl(38),.mul(1,2)mul(3,3333)sjsjX"
TEST_DATA = "xyxmul(100,456)xyzmuöl(38),.mul(1,2)mul(3,10)sjsjX"


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


def parse_data(data: str = TEST_DATA, verbose: int = 0) -> list:
    """
        parse_data()
            Extracts valid tokens (substrings of the form 'mul(x,y)', where x and y
            are integers) from a string.

            Returns a list of token-strings.
    """
    valid_tokens = []  # A list that will hold valid tokens ('mul(x,y)'-substrings)
    valid = True  # Indicator that a token is (still) valid
    eof = False  # flag that indicates whether we have reached end-of-file (end-of-data)
    k = 0  # index into to the data
    while valid and not eof:
        try:
            # Set token-length
            l = 4
            # Check that we do not go beoynd the length of the data
            if k + l > len(data):
                eof = True
                continue
            # Get next token
            token = get_token(data, k, l)
            # If token does not match the beginning of a 'mul(x,y)' operation
            # move one step forward and start the while-loop over
            if token != "mul(":
                k += 1
                continue
            # Increase token-length by 1
            l += 1
            # Loop while the token ends in a digit
            while get_token(data, k, l)[-1] in digits:
                token = get_token(data, k, l)
                l += 1
            # If the token now ends with a ",", update the token
            # and investigate further
            if get_token(data, k, l)[-1] == ",":
                token = get_token(data, k, l)
                l += 1
                # Again, if the token ends with a digit, increase token-length
                # by one, update the token, and and repeat until the token
                # does not end with a digit
                while get_token(data, k, l)[-1] in digits:
                    token = get_token(data, k, l)
                    l += 1
                # Token now ends with a non-digit. If it ends with a ")",
                # we have found a valid token, so we add it to the list of
                # valid tokens
                if get_token(data, k, l)[-1] == ")":
                    token = get_token(data, k, l)
                    valid_tokens.append(token)
                    l += 1
                    if verbose > 0:
                        print(token)
            k += len(token)
        except IndexError:
            pass
    if verbose > 0:
        print(valid_tokens)
    return valid_tokens


def main() -> None:
    """main()"""
    tokens = parse_data(TEST_DATA, verbose=1)
    token_sum = 0
    # pylint: disable=eval-used
    for token in tokens:
        token_sum += eval(token)
    print(f"Sum of mul()-tokens = {token_sum}")
    print(f"Number of mul()-tokens = {len(tokens)}")


if __name__ == "__main__":
    main()
