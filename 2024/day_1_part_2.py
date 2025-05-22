"""
    Advent of Code 2024
    Day 1, part 2

    The first half of this puzzle is complete! It provides one gold star: *
    Your puzzle answer was 2367773.

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
"""

# pylint: disable=unused-import
import numpy as np
import pandas as pd
# pylint: enable=unused-import

# pylint: disable=import-error
from day_1_part_1 import import_data  # , sort_data
# pylint: enable=import-error

def day_1_part_2():
    """day_1_part_2()"""

    def similarity_score():
        """Compute similarity score as described above"""
        score = 0
        for val_c1 in df.C1:  # For every value in column 1...
            # Select from the second column the values
            # which are equal to the current value of
            # columnt 1
            n_val_c1_in_c2 = len(df.loc[df.C2 == val_c1])
            # Multiply the number of occurrences with the
            # current column-one-value
            score += (n_val_c1_in_c2 * val_c1)
        return score

    # Import data to dataframe
    # df = import_data(1, example=True)
    df = import_data(1)

    # Compute and print the similarity score
    print(similarity_score())


def main():
    """main() - a redundant level of indirection..."""
    day_1_part_2()


if __name__ == "__main__":
    main()
