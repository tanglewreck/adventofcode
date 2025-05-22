# xmypy: xdisable_error_code="call-overload"

"""
    Advent of Code 2024
    Day 1

   --- Day 1: Historian Hysteria ---

    The Chief Historian is always present for the big Christmas sleigh launch,
    but nobody has seen him in months! Last anyone heard, he was visiting
    locations that are historically significant to the North Pole; a group of
    Senior Historians has asked you to accompany them as they check the places
    they think he was most likely to visit.

    As each location is checked, they will mark it on their list with a star.
    They figure the Chief Historian must be in one of the first fifty places
    they'll look, so in order to save Christmas, you need to help them get
    fifty stars on their list before Santa takes off on December 25th.

    Collect stars by solving puzzles. Two puzzles will be made available on
    each day in the Advent calendar; the second puzzle is unlocked when you
    complete the first. Each puzzle grants one star. Good luck!

    You haven't even left yet and the group of Elvish Senior Historians has
    already hit a problem: their list of locations to check is currently empty.
    Eventually, someone decides that the best place to check first would be the
    Chief Historian's office.

    Upon pouring into the office, everyone confirms that the Chief Historian is
    indeed nowhere to be found. Instead, the Elves discover an assortment of
    notes and lists of historically significant locations! This seems to be the
    planning the Chief Historian was doing before he left. Perhaps these notes
    can be used to determine which locations to search?

    Throughout the Chief's office, the historically significant locations are
    listed not by name but by a unique number called the location ID. To make
    sure they don't miss anything, The Historians split into two groups, each
    searching the office and trying to create their own complete list of
    location IDs.

    There's just one problem: by holding the two lists up side by side (your
    puzzle input), it quickly becomes clear that the lists aren't very similar.
    Maybe you can help The Historians reconcile their lists?

    For example:

    3   4
    4   3
    2   5
    1   3
    3   9
    3   3

    Maybe the lists are only off by a small amount! To find out, pair up the
    numbers and measure how far apart they are. Pair up the smallest number in
    the left list with the smallest number in the right list, then the
    second-smallest left number with the second-smallest right number, and so
    on.

    Within each pair, figure out how far apart the two numbers are; you'll need
    to add up all of those distances. For example, if you pair up a 3 from the
    left list with a 7 from the right list, the distance apart is 4; if you
    pair up a 9 with a 3, the distance apart is 6.

    In the example list above, the pairs and distances would be as follows:

    The smallest number in the left list is 1, and the smallest number in the
    right list is 3. The distance between them is 2.  The second-smallest
    number in the left list is 2, and the second-smallest number in the right
    list is another 3. The distance between them is 1.  The third-smallest
    number in both lists is 3, so the distance between them is 0.  The next
    numbers to pair up are 3 and 4, a distance of 1.  The fifth-smallest
    numbers in each list are 3 and 5, a distance of 2.  Finally, the largest
    number in the left list is 4, while the largest number in the right list is
    9; these are a distance 5 apart.

    To find the total distance between the left list and the right list, add up
    the distances between all of the pairs you found. In the example above,
    this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

    Your actual left and right lists contain many location IDs. What is the
    total distance between your lists?


"""

# Get the data
# Sort columns
# For each row, compute the distance. Add to 'total_distance'

import sys
import numpy as np
import pandas as pd
from pandas.core.generic import NDFrame

# pylint: disable=unspecified-encoding

DATAPROD = "day_1_data"
DATAEXAMPLE = "day_1_data_example"
DATA = DATAEXAMPLE

def import_data(nday: int, example=False) -> pd.DataFrame | None:
    """
        import_data
            Read a comma-separated datafile.
            Return a pandas.DataFrame
    """
    fname = "day_" + str(nday) + "_data"
    if example:
        fname += "_example"
    try:
        with open(fname) as fp:
            return pd.read_csv(fp, sep=",")
    except (OSError, pd.errors.ParserError) as e:
        print(repr(e), file=sys.stderr)
    return None


def export_data(df: pd.DataFrame, nday: int,
                       example=False) -> pd.DataFrame | None:
    """
        export_data
            Sort and export a dataframe to a
            comma-separated (csv) file.
    """
    fname = "day_" + str(nday) + "_sorted_data"
    if example:
        fname += "_example"
    try:
        for column in df.columns:
# mypy: disable_error_code="call-overload"
            np.asarray(df[column]).sort()
        df.to_csv(fname, sep=",", index=None)
        return df
    except (OSError, pd.errors.ParserError) as e:
        print(repr(e), file=sys.stderr)
        return None
    return None


def sort_data(df: pd.DataFrame) -> pd.DataFrame | None:
    """
        Sort dataframe columns 
    """
    for column in df.columns:
# mypy: disable_error_code="call-overload"
        np.asarray(df[column]).sort()


def day_1():
    """day_1()"""
    # Import data
    # df = import_data(nday=1, example=False)
    df = import_data(nday=1, example=False)
    # df = pd.read_table(DATAEXAMPLE, sep=",")
    # Sort columns
    np.asarray(df["C1"]).sort()
    np.asarray(df["C2"]).sort()
    sort_data(df)
    df = export_data(df, 1, example=False)

    # Print result
    s = sum(abs(df["C1"] - df["C2"]))
    print(f"1. sum of differences = {s}")


    # Alternative approach:
    c1, c2 = [], []
    # pylint: disable=consider-using-with
    for k, row in enumerate(open(DATA)):
        if k:
            d = [int(x) for x in row.strip().split(",")]
            c1.append(d[0])
            c2.append(d[1])
    s = 0
    c1.sort()
    c2.sort()
    for k, x in enumerate(c1):
        s += abs(x - c2[k])
    print(f"2. sum of differences = {s}")

    # Another approach which makes the linter happy:
    with open(DATA, encoding="utf-8") as fp:
        s = 0
        c1, c2 = [], []
        while row := fp.readline():
            if "C" in row:
                continue
            c = [int(x) for x in row.strip().split(",")]
            c1.append(c[0])
            c2.append(c[1])
        c1.sort()
        c2.sort()
        for k, c in enumerate(c1):
            s += abs(c - c2[k])
        print(f"3. sum of differences = {s}")


def main():
    """main()"""
    day_1()


if __name__ == "__main__":
    main()
