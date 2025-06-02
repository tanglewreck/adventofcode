# vim: set numberwidth=4 number expandtab textwidth=79 noignorecase :
"""

    --- Day 5: Print Queue ---

    Satisfied with their search on Ceres, the squadron of scholars suggests
    subsequently scanning the stationery stacks of sub-basement 17.

    The North Pole printing department is busier than ever this close to
    Christmas, and while The Historians continue their search of this
    historically significant facility, an Elf operating a very familiar printer
    beckons you over.

    The Elf must recognize you, because they waste no time explaining that the
    new sleigh launch safety manual updates won't print correctly. Failure to
    update the safety manuals would be dire indeed, so you offer your services.

    Safety protocols clearly indicate that new pages for the safety manuals
    must be printed in a very specific order. The notation X|Y means that if
    both page number X and page number Y are to be produced as part of an
    update, page number X must be printed at some point before page number Y.

    The Elf has for you both the page ordering rules and the pages to produce
    in each update (your puzzle input), but can't figure out whether each
    update has the pages in the right order.

    For example:

    47|53
    97|13
    97|61
    97|47
    75|29
    61|13
    75|53
    29|13
    97|29
    53|29
    61|53
    97|53
    61|29
    47|13
    75|47
    97|75
    47|61
    75|61
    47|29
    75|13
    53|13

    75,47,61,53,29
    97,61,53,29,13
    75,29,13
    75,97,47,61,53
    61,13,29
    97,13,75,29,47

    The first section specifies the page ordering rules, one per line. The
    first rule, 47|53, means that if an update includes both page number 47
    and page number 53, then page number 47 must be printed at some point
    before page number 53. (47 doesn't necessarily need to be immediately
    before 53; other pages are allowed to be between them.)

    The second section specifies the page numbers of each update. Because
    most safety manuals are different, the pages needed in the updates are
    different too. The first update, 75,47,61,53,29, means that the update
    consists of page numbers 75, 47, 61, 53, and 29.

    To get the printers going as soon as possible, start by identifying
    which updates are already in the right order.

    In the above example, the first update (75,47,61,53,29) is in the right
    order:

        – 75 is correctly first because there are rules
        that put each other page after it: 75|47, 75|61,
        75|53, and 75|29.

        – 47 is correctly second because 75 must be before
        it (75|47) and every other page must be after it
        according to 47|61, 47|53, and 47|29.

        – 61 is correctly in the middle because 75 and 47
        are before it (75|61 and 47|61) and 53 and 29 are
        after it (61|53 and 61|29).

        – 53 is correctly fourth because it is before page
        number 29 (53|29).

        – 29 is the only page left and so is
        correctly last.

    Because the first update does not include some page numbers, the ordering
    rules involving those missing page numbers are ignored.

    The second and third updates are also in the
    correct order according to the rules. Like the
    first update, they also do not include every page
    number, and so only some of the ordering rules
    apply - within each update, the ordering rules that
    involve missing page numbers are not used.

    The fourth update, 75,97,47,61,53, is not in the
    correct order: it would print 75 before 97, which
    violates the rule 97|75.

    The fifth update, 61,13,29, is also not in the
    correct order, since it breaks the rule 29|13.

    The last update, 97,13,75,29,47, is not in the
    correct order due to breaking several rules.

    For some reason, the Elves also need to know the
    middle page number of each update being printed.
    Because you are currently only printing the
    correctly-ordered updates, you will need to find
    the middle page number of each correctly-ordered
    update. In the above example, the correctly-ordered
    updates are:

    75,47,61,53,29
    97,61,53,29,13
    75,29,13

    These have middle page numbers of 61, 53, and 29
    respectively. Adding these page numbers together
    gives 143.

    Of course, you'll need to be careful: the actual
    list of page ordering rules is bigger and more
    complicated than the above example.

    Determine which updates are already in the correct
    order.

    What do you get if you add up the middle page
    number from those correctly-ordered updates?

    -->  <--

"""
import os
import pathlib
from pathlib import Path
import sys
# from utils.as_dataframe import as_dataframe
# from helpers.day_4_pt2 import x_mas_list, x_mas_pd, x_mas_np
from helpers import __DATADIR__

# from collections import defaultdict
from helpers.day_5_part_1 import get_data
# from helpers.day_5_part_1 import get_data, build_rules
# from helpers.day_5_part_1 import UPDATES, RULES_EXAMPLE

# Constants
__NAME__ = "day_5"  # this is us
__PART__ = "1"


def get_input_file(example=False):
    """get_input_file"""
    #
    # import argparse
    #
    # Check for a commandline argument and use that as
    # the path to the file containing the input data
    try:
        input_file = Path(sys.argv[1])
        if not os.access(input_file, os.R_OK):
            raise OSError
    except OSError as exception:
        raise SystemExit("No such file") from exception
    except IndexError:
        # Default data input
        if example:
            input_file = pathlib.Path(
                    f"{__DATADIR__}/{__NAME__}_part_{__PART__}_example_2")
        else:
            input_file = pathlib.Path(
                    f"{__DATADIR__}/{__NAME__}_part_{__PART__}")
    return input_file


def main(verbose: int = 0):
    """main"""

#     def check_post_rules():
#         """check rules for succeeding items"""
#         for cur_index, cur_item in enumerate(update):
#             n = len(update)
#             # check that the current item (page-number) does not occur
#             # in any of the rules for the following page-numbers
#             for post_item in update[cur_index + 1: n]:
#                 # if the current item does not occur in any rule for
#                 # the items that follow it, then we're good
#                 # ok = post_item in rules[cur_item]  # this one, or
#                 ok = cur_item not in rules[post_item]  # this one...
#                 if verbose > 1:
#                     print(f"{post_item} in rules[{cur_item}] = {ok}")
#                 if not ok:
#                     all_ok = False
#                     update_ok = False

    # Get name of input file
    input_file = get_input_file(example=False)
    # Import data
    rules, updates = get_data(input_file)
    # rules = build_rules()
    # print(f"rules: {rules}")
    all_ok = True
    n_ok = 0
    # collect the sum of the middle element of each valid update
    sum_mid_pages: int = 0
    # verify updates; for valid updates, add the middle page-number
    # to the sum of mid-pages (sum_mid_pages)
    for k, update in enumerate(updates):
        update_ok = True
        if verbose > 1:
            print(f"update[{k}]: {update}")
        # walk through each update and check that for each
        # page-number and for each page-numbers following
        # that page-number, no rule stipulates that one of
        # succeeding page-numbers should precede the page-number
        # being checked; if that is the case, the update is
        # invalid; if there's no conflicting rule, the update
        # is valid
        for cur_index, cur_item in enumerate(update):
            n = len(update)
            # check that the current item (page-number) does not occur
            # in any of the rules for the following page-numbers
            for post_item in update[cur_index + 1: n]:
                # if the current item does not occur in any rule for
                # the items that follow it, then we're good
                # ok = post_item in rules[cur_item]  # this one, or
                ok = cur_item not in rules[post_item]  # this one...
                if verbose > 1:
                    print(f"{post_item} in rules[{cur_item}] = {ok}")
                if not ok:
                    all_ok = False
                    update_ok = False
        if update_ok:
            n_ok += 1
            if verbose:
                print(f"update[{k}]: OK")
            len_update = len(update)
            if len_update % 2 != 1:
                print(f"len(update[{k}]) is even: BAD")
            else:
                mid_index = int((len_update - 1) / 2)
                sum_mid_pages += update[mid_index]
                if verbose:
                    # print(f"updates[{k}] = {update}")
                    # print(f"len(update[{k}])= {len_update}")
                    # print(f"mid index (update[{k}]) = {mid_index}")
                    print(f"mid = {update[mid_index]}")
                    print(f"sum = {sum_mid_pages}")
        else:
            if verbose > 1:
                print(f"update[{k}]: NOT ok")
        # print()
    empty_rules = False
    for rulenum, rulelist in rules.items():
        if not rulelist:
            empty_rules = True
            if verbose:
                print(f"rule {rulenum} is empty ({rulelist})")
    if empty_rules:
        print("empty rules found")
    else:
        print("NO empty rules found")
    print(f"all_ok = {all_ok}")
    print(f"number of OK updates = {n_ok}")
    print(f"sum of mid pages = {sum_mid_pages}")


if __name__ == "__main__":
    main()
