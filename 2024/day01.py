"""
    Advent of Code 2024
    Day 1, part 1

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

        --> 2367773 <--

    The first half of this puzzle is complete! It provides one gold star: *

    --- Part Two ---

    Your analysis only confirmed what everyone feared: the two lists of
    location IDs are indeed very different.

    Or are they?

    The Historians can't agree on which group made the mistakes or how to read
    most of the Chief's handwriting, but in the commotion you notice an
    interesting detail: a lot of location IDs appear in both lists! Maybe the
    other numbers aren't location IDs at all but rather misinterpreted
    handwriting.

    This time, you'll need to figure out exactly how often each number from the
    left list appears in the right list. Calculate a total similarity score by
    adding up each number in the left list after multiplying it by the number
    of times that number appears in the right list.

    Here are the same example lists again:

    3   4
    4   3
    2   5
    1   3
    3   9
    3   3

    For these example lists, here is the process of finding the similarity
    score:

    The first number in the left list is 3. It appears in the right list three
    times, so the similarity score increases by 3 * 3 = 9.  The second number
    in the left list is 4. It appears in the right list once, so the similarity
    score increases by 4 * 1 = 4.  The third number in the left list is 2. It
    does not appear in the right list, so the similarity score does not
    increase (2 * 0 = 0).  The fourth number, 1, also does not appear in the
    right list.  The fifth number, 3, appears in the right list three times;
    the similarity score increases by 9.  The last number, 3, appears in the
    right list three times; the similarity score again increases by 9.

    So, for these example lists, the similarity score at the end of this
    process is 31 (9 + 4 + 0 + 0 + 9 + 9).

    Once again consider your left and right lists. What is their similarity
    score?

    ------------------------------------------------------------------------
    similarity score = 21271939

    That's the right answer! You are one gold star closer to finding the Chief
    Historian.

    You have completed Day 1!
    ------------------------------------------------------------------------

"""

import argparse
import numpy as np
import pandas as pd
from utils import import_data
# from utils import export_data


# this is day 1
__DAYNUM__ = 1


def sort_data(df: pd.DataFrame) -> None:
    """
        Sort dataframe columns
    """
    for column in df.columns:
        np.asarray(df[column]).sort()


def part_1(example: bool = False, verbose: int = 0):
    """day_1()"""
    # The Plan:
    #   - Get the data
    #   - Sort columns
    #   - For each row, compute the distance. Add to 'total_distance'
    # Import data
    df = import_data(day=1, part=1, example=example)
    # Sort columns
    sort_data(df)
    if verbose > 0:
        print(df)
    # export data (to csv)
    # export_data(df, 1, example=example)

    # Print result
    sum_diff_c1_c2 = sum(abs(df.loc[:, "C1"] - df.loc[:, "C2"]))
    print(f"sum of differences = {sum_diff_c1_c2}")


def part_2(example: bool = False, verbose: int = 0):
    """part_2()"""

    def similarity_score():
        """Compute similarity score as described above"""
        score = 0
        for val_c1 in df.C1:  # For every value in column 1...
            # select from the second column the values
            # which are equal to the current value of
            # column 1
            n_val_c1_in_c2 = len(df.loc[df.C2 == val_c1])
            # multiply the number of occurrences with the
            # current column-one-value
            score += (n_val_c1_in_c2 * val_c1)
        return score

    # import data to dataframe
    # use the same datafile as in part 1
    df = import_data(day=1, part=1, example=example)
    if verbose > 0:
        print(df)

    # compute and print the similarity score
    print(f"Similarity score = {similarity_score()}")


def main():
    """main()"""
    parser = argparse.ArgumentParser(description=f"aoc 2024 day {__DAYNUM__}",
                                     prog=f"day_{__DAYNUM__}",
                                     add_help=True)
    parser.add_argument('--part', type=int, default=1,
                        choices=[1, 2],
                        help='part number (1 or 2)')
    parser.add_argument('--example', default=False,
                        action='store_true',
                        help='use example datafile')
    parser.add_argument('--input', type=argparse.FileType('r'),
                        help='not used')
    parser.add_argument('--verbose', type=int, default=0,
                        choices=[0, 1, 2],
                        help='get diagnostics')
    args = parser.parse_args()
    if args.part == 1:
        part_1(args.example, args.verbose)
    else:
        part_2(args.example, args.verbose)


if __name__ == "__main__":
    main()
