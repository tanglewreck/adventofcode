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
# import pandas as pd
# pylint: enable=unused-import

# pylint: disable=import-error
from day_1_part_1 import import_data  # , sort_data
# pylint: enable=import-error


def check_row_safety(row: np.ndarray,
                     row_num: int = 0,
                     verbose=0) -> bool | None:
    """
        Check a sequence of numbers for 'safety':

        A sequence is considered safe if
            1. the sequence is monotonically and strictly
               increasing or decreasing (all differences
               between successive elements have the same sign
               and is not zero), and
            2. the absolute value of the difference between any pair
               of successive elements less than or equal to 3.

        In other words, if a is a sequence (a zero-based array) of real
        numbers of length n, i ∈ ℕ: i ∈ (0, n - 1), and
        d[i] = a[i] - a[i+1] is the difference between two successive
        elements in that array, then , a is safe iff
            1. d[i] > 0 or diff[i] < 0, for all i ∈ (0, n - 1), and
            2. abs(d[i]) <= 3 for all i ∈ (0, n - 1).

    """
    if len(row) <2:
        return None
    # Create two temp-arrays
    tmparr1 = np.append([0], row)  # add zero at the start
    tmparr2 = np.append(row, [0])  # add zero at the end
    # Calculate the difference btw the temp-arrays;
    # this gives us the differences between successive
    # elements in the input array (the first and last
    # diffs are discarded since we are only interested
    # in the 'internal' differences between elements)
    diffarr = tmparr2 - tmparr1
    diffarr = diffarr[1:len(row)]  # Lose first and last elements
    # Print diagnostics if verbose
    if verbose > 2:
        print("row:", row, f"({len(row)})")
        print("tmparr1:", tmparr1, f"({len(tmparr1)})")
        print("tmparr2:", tmparr2, f"({len(tmparr2)})")
        print("diffarr:", diffarr, f"({len(diffarr)})")
    if verbose > 1:
        # A row is not safe unless all diffs have the same sign
        if not all(diffarr > 0) and not all(diffarr < 0):
            print(f"Row {row_num:003d} NOT safe: SIGN change: {list(row)}")
        # A row is not safe unless all diffs are less than or equal to 3
        if not all(abs(diffarr) <= 3):
            print(f"Row {row_num:003d} NOT safe: diff TOO LARGE: {list(row)}")
    if verbose > 0:
        # A row is safe if all diffs have same sign, and  all diffs
        # are less than or equal to 3:
        safe = (all(diffarr > 0) or all(diffarr < 0)) \
                and all(abs(diffarr) <= 3)
        if safe:
            print(f"Row {row_num:003d} SAFE: {list(row)}")
    # Return true if all diffs have same sign, and  all diffs
    # are less than or equal to 3:
    return (all(diffarr > 0) or all(diffarr < 0)) and all(abs(diffarr) <= 3)


# - - - - - - -
# OLD VERSION
# - - - - - - -
# def day_2_part_1():
#     """day_2_part_1()"""
#
#     # Import data to dataframe
#     df = import_data(2, example=False)
#     nsafe_reports, nrows = check_safety(df, 0, len(df) - 1, verbose=2)
#     print(f"Number of safe reports = {nsafe_reports} (out of {nrows})")


def day_2_part_1():
    """day_2_part_1()"""
    # Import data to dataframe
    df = import_data(2, example=False)
    # Count the number of safe rows (reports)
    nsafe_reports = 0
    # For each row in the data frame...
    for k in range(df.shape[0]):  # shape is (1000, 8)
        # Convert the row to a list (so that we can drop zeros at
        # the end; np.ndarrays do no allow this)
        row = list(df.iloc[k, ])
        # As long as there are zeros at the end of the list,
        # drop them.
        while row[-1] == 0:
            row = row[:-1]
        # Now, check if the row/report is safe
        if check_row_safety(row, k, verbose=0):
            nsafe_reports += 1
    print(f"Number of safe reports = {nsafe_reports} (out of {df.shape[0]})")


def main():
    """main() - a redundant level of indirection..."""
    day_2_part_1()


if __name__ == "__main__":
    main()
