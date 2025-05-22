"""
    --- Day 2: Red-Nosed Reports ---

    Fortunately, the first location The Historians want to search isn't a long
    walk from the Chief Historian's office.

    While the Red-Nosed Reindeer nuclear fusion/fission plant appears to
    contain no sign of the Chief Historian, the engineers there run up to you
    as soon as they see you. Apparently, they still talk about the time Rudolph
    was saved through molecular synthesis from a single electron.

    They're quick to add that - since you're already here - they'd really
    appreciate your help analyzing some unusual data from the Red-Nosed
    reactor. You turn to check if The Historians are waiting for you, but they
    seem to have already divided into groups that are currently searching every
    corner of the facility. You offer to help with the unusual data.

    The unusual data (your puzzle input) consists of many reports, one report
    per line. Each report is a list of numbers called levels that are separated
    by spaces. For example:

    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9

    This example data contains six reports each containing five levels.

    The engineers are trying to figure out which reports are safe. The
    Red-Nosed reactor safety systems can only tolerate levels that are either
    gradually increasing or gradually decreasing. So, a report only counts as
    safe if both of the following are true:

    The levels are either all increasing or all decreasing.  Any two adjacent
    levels differ by at least one and at most three.

    In the example above, the reports can be found safe or unsafe by checking
    those rules:

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

    So, in this example, 2 reports are safe.

    Analyze the unusual data from the engineers. How many reports are safe?

    ------------------------------------------------------------
    Your puzzle answer was 282.

    The first half of this puzzle is complete! It provides one gold star: *
    ------------------------------------------------------------

"""


# pylint: disable=unused-import
import numpy as np
import pandas as pd
# pylint: enable=unused-import

# pylint: disable=import-error
from day_1_part_1 import import_data  # , sort_data
# pylint: enable=import-error

# pylint: disable=too-many-branches
def check_safety(df, begin: int = 0, end: int|None = None, verbose=0) -> bool:
    """evaluate report-safety"""
    # Sanity checks
    if not end:
        end = len(df) - 1
    assert begin < end
    assert begin >= 0 and end < len(df)
    # Initialise counter
    nsafe = 0
    nrows = 0
    for i in range(begin, end + 1):
        is_safe = True
        nrows += 1
        row = np.asarray(df.iloc[i, ])
        lastdiff = row[1] - row[0]
        if abs(lastdiff) < 1 or abs(lastdiff) > 3:
            if verbose > 1:
                print(f"Row {i:003d} NOT safe: diff to LARGE: ", end="")
                print(f"(diff = {lastdiff}, j=0): ", end="")
                print(f"Row = {row}")
            is_safe = False
            continue
        for j in range(1, len(row) - 1):
            if row[j] == 0 or row[j + 1] == 0:
                break
            diff = row[j+1] - row[j]
            if lastdiff * diff <= 0:
                if verbose > 1:
                    if lastdiff * diff < 0:
                        print(f"Row {i:003d} NOT safe: SIGN change: ", end="")
                    else:  # verbosity >= 2
                        print(f"Row {i:003d} NOT safe: NO change: ", end="")
                    print(f"({lastdiff * diff}, j={j}): ", end="")
                    print(f"Row = {row}")
                is_safe = False
                break
            if abs(diff) > 3 or abs(diff) < 1:
                if verbose > 1:
                    print(f"Row {i:003d} NOT safe: diff to LARGE: ", end="")
                    print(f"(diff = {diff}, j={j}): ", end="")
                    print(f"Row = {row}")
                is_safe = False
                break
            lastdiff = diff
        if is_safe:
            nsafe += 1
            if verbose > 0:
                print(f"Row {i:003d} SAFE: ", end="")
                print(row)
    return nsafe, nrows


def day_2_part_2():
    """day_2_part_2()"""

    # Import data to dataframe
    df = import_data(2, example=False)
    nsafe_reports, nrows = check_safety(df, 0, len(df) - 1, verbose=2)
    print(f"Number of safe reports = {nsafe_reports} (out of {nrows})")


def main():
    """main() - a redundant level of indirection..."""
    day_2_part_2()


if __name__ == "__main__":
    main()
