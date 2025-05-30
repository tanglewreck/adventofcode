"""day_3_part_2 snippet"""

# pylint: disable=unused-import
import re
from string import digits


# pylint: disable=unused-variable
TESTSTRING = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
# pylint: enable=unused-variable


def mul(x: int|float, y: int|float = 1) -> int|float:
    """Multiply two numbers"""
    return x * y



def get_token(data:str, index:int, length:int) -> str:
    """get_token()"""
    return data[index : index + length]


def get_data() -> str:
    """get_data()"""
    try:
        with open("data/day_3_data_stripped") as fp:
            return fp.read().strip()
    except OSError as exception:
        print(f"{repr(exception)}")
        raise SystemExit(1) from exception



def main(verbose = 1) -> None:
    """main()"""

    data = d = get_data()

    if verbose > 0:
        print(f"data is {len(data)} characters long")
    # mul_characters = "mul,()" + digits
    # curr_c = d[0]
    muls = []
    do = True
    print("Processing...")
    # pylint: disable=too-many-nested-blocks
    for k, _ in enumerate(d):
        try:
            # get token = the next 3 characters
            token = get_token(data, k, 4)
            # check for "do()"
            do = get_token(data, k, 4) == "do()"
            # check for "don't()"
            do = not get_token(data, k, 7) == "don't()"

            # If we've found the string 'mul(', investigate further...
            if token == "mul(":
                # We still have a valid token...
                valid = True
                i = 3  # offset
                token_length = 5
                while valid:
                    # extend token
                    while get_token(data, k, token_length)[-1] in digits:
                        token = get_token(data, k, token_length)
                        token_length += 1
                    if get_token(data, k, token_length) == ",":
                        token = get_token(data, k, token_length)
                        token_length += 1
                        while get_token(data, k, token_length)[-1] in digits:
                            token = get_token(data, k, token_length)
                            token_length += 1
                    # get next character
                    c = d[k+i]
                    i += 1
                    if c != "(":
                        valid = False
                        break
                    token += "("
                    c = d[k+i]
                    i += 1
                    while c in digits + ",":
                        if c == "," and d[k+i+1] not in digits:
                            valid = False
                            break
                        token += c
                        c = d[k+i]
                        i += 1
                    # if not valid:
                     #   break
                    if not c == ")":
                        valid = False
                        continue
                    token += c
                    if do:
                        # print(token)
                        if "," in token:
                            muls.append(token)
        except IndexError:
            pass
    # print(muls)
    mul_sum = 0
    for m in muls:
        # pylint: disable=eval-used
        mul_sum += eval(m)
        # print(m)
    print(f"{len(muls)} mul() operations")
    print(f"sum of mul() operations = {mul_sum}")


if __name__ == "__main__":
    main()
