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


    --- Part Two ---

    The engineers are surprised by the low number of safe reports until they
    realize they forgot to tell you about the Problem Dampener.

    The Problem Dampener is a reactor-mounted module that lets the reactor
    safety systems tolerate a single bad level in what would otherwise be a
    safe report. It's like the bad level never happened!

    Now, the same rules apply as before, except if removing a single level from
    an unsafe report would make it safe, the report instead counts as safe.

    More of the above example's reports are now safe:

    7 6 4 2 1: Safe without removing any level.
    1 2 7 8 9: Unsafe regardless of which level is removed.
    9 7 6 2 1: Unsafe regardless of which level is removed.
    1 3 2 4 5: Safe by removing the second level, 3.
    8 6 4 4 1: Safe by removing the third level, 4.
    1 3 6 7 9: Safe without removing any level.

    Thanks to the Problem Dampener, 4 reports are
    actually safe!

    Update your analysis by handling situations where
    the Problem Dampener can remove a single level from
    unsafe reports. How many reports are now safe?

    --> 349 <--

    That's the right answer! You are one gold star closer
    to finding the Chief Historian.


"""

from day_1_part_1 import import_data
from day_2_part_1 import check_row_safety
# pylint: enable=import-error


def recheck_row(row, verbose=0) -> bool | None:
    """
        recheck_row()
            Recheck a row by popping off one item at a time
            and running the popped row through the row-checker.

            Returns true if either the row is safe to begin with
            or if it is safe with one item removed (stops checking
            when the one item removed makes the row safe; there might
            be other items which could be removed to make the row safe).
    """
    if not (now_safe := check_row_safety(row)):
        for i, _ in enumerate(row):
            # Make a copy so that we can check the row
            # multiple times
            temp_row = row.copy()
            # Pop an item
            removed_item = temp_row.pop(i)
            if verbose > 1:
                print(f"Item {i} popped from temp_row: {temp_row}")
            # Test the row with the item removed
            if now_safe := check_row_safety(temp_row):
                if verbose > 1:
                    print(f"original row: {temp_row}")
                    print(f"popped row: {temp_row}")
                    print()
                if verbose > 0:
                    print(f"safe with item {i} removed: {removed_item}: ")
                # Break out of the for-loop if the modified row is safe
                break
        # If the row is unsafe no matter which item is removed,
        # barf (if verbosity is high enough)
        if not now_safe:
            if verbose > 0:
                print("not safe, no matter what")
    else:
        if verbose > 0:
            print("already safe")
    # Return True/False depending on if the row can be made
    # safe or not.
    return now_safe


def day_2_part_2():
    """day_2_part_2()"""
    # Import data to dataframe
    df = import_data(2, example=False)
    # Count the number of safe rows (reports)
    n_safe_reports = 0
    n_salvagable_reports = 0
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
            n_safe_reports += 1
        else:  # Re-check row with one item removed
            if recheck_row(row):
                # print(f"Row {k:003d} is salvagable: {row}")
                n_salvagable_reports += 1
    print("Number of originally safe reports = "
          f"{n_safe_reports}")
    print("Number of salvagable reports = "
          f"{n_salvagable_reports}")
    print("Number of safe reports (total) = "
          f"{n_safe_reports + n_salvagable_reports}")
    print("Number of unsafe reports = "
          f"{df.shape[0] - n_salvagable_reports - n_safe_reports}"
          f"(out of {df.shape[0]})")


def main():
    """main() - a redundant level of indirection..."""
    day_2_part_2()


if __name__ == "__main__":
    main()
