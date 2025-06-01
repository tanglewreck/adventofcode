"""
    cli.py
"""

import argparse


def day_number(num):
    """ day_number """
    if len(num) > 4 or not num.isdigit():
        # pylint: disable=no-value-for-parameter
        raise argparse.ArgumentError(f"Invalid day number format: {num}")

    return num.zfill(4)


def get_args():
    """
        get_args()
    """
    parser = argparse.ArgumentParser(
            prog="day", description="Run selected day")
    parser.add_argument("day", type=day_number,
                        help="The number of the day you wish to run")
    parser.add_argument("-v", "--verbose", action="store_true",
                        dest="verbose", default=False, help="Verbose output")

    args = parser.parse_args()
    return args
