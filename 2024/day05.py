#!/usr/bin/env python
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

    --> 4135  <--

    The first half of this puzzle is complete! It provides one gold star: *
    --- Part Two ---

    While the Elves get to work printing the correctly-ordered updates, you
    have a little time to fix the rest of them.

    For each of the incorrectly-ordered updates, use the page ordering rules to
    put the page numbers in the right order. For the above example, here are
    the three incorrectly-ordered updates and their correct orderings:

        75,97,47,61,53 becomes 97,75,47,61,53.
        61,13,29 becomes 61,29,13.
        97,13,75,29,47 becomes 97,75,47,29,13.
    for each element in the update
        check the rules for all suceeding elements
            if the current element occurs in a rule,
            pop the current element and shift all elements
            up to the element in who's rule the current element
            occur to the left and place the current element there instead

            define a function who returns true if the element being
            checked occurs in the reference value's rule (which states
            what elements must suceed it), then use that function as
            the sort-function argument to sorted()

    After taking only the incorrectly-ordered updates and ordering
    them correctly, their middle page numbers are 47, 29, and 47.
    Adding these together produces 123.

    Find the updates which are not in the correct order. What do
    you get if you add up the middle page numbers after correctly
    ordering just those updates?

    --> 5285 <--

"""

# from collections import defaultdict
import argparse
from collections import defaultdict
from typing import DefaultDict, List  # , Tuple
from helpers.day_5_rules_and_updates import get_rules_and_updates
from helpers.day_5_fix import fix_updates
from helpers.day_5_valid import update_is_valid
from helpers.day_5_verify import verify_updates
from utils.get_data_path import get_data_path
from utils.verbose_msg import verbose_msg

# Constants
__DAYNUM__ = 5  # this is us
__PART__ = 1


def check_for_empty_rules(rules, verbose=0):
    """check for empty rules"""
    empty_rules = False
    for rulenum, rulelist in rules.items():
        if not rulelist:
            empty_rules = True
            verbose_msg(f"rules[{rulenum}] is empty ({rulelist})", 1, verbose)
    return empty_rules


def part_1(example: bool, verbose: int = 0):
    # -> Tuple[List[List[int]], List[int]]:
    # List[int]:
    """
        part 1()
            - returns a tuple of (lists of) valid and invalid updates
            - if example is True, example data is used; otherwise
              the full data is used
    """
    print("= " * 10)
    print(" PART 1")
    print("= " * 10)
    # Get name of input file
    data_path = get_data_path(__DAYNUM__, __PART__, example=example)
    # Import data
    rules: DefaultDict[int, list[int]] = defaultdict(lambda: [])
    updates: List[List[int]] = []
    rules, updates = get_rules_and_updates(data_path)
    all_updates_ok = True
    n_valid_rules = 0
    # collect the sum of the middle element of each valid update
    sum_mid_valid: int = 0
    sum_mid_all: int = 0
    # verify updates; for valid updates, add the middle page-number
    # to the sum of mid-pages (sum_mid_valid); also, collect the indices
    # of valid and invalid updates, respectively
    valid_updates: List[int] = []
    invalid_updates: List[int] = []
    for update_index, update in enumerate(updates):
        len_update = len(update)
        mid_index = int(len_update / 2)
        update_valid = True
        verbose_msg(f"update[{update_index}]: {update}", 1, verbose)
        # walk through each update and check that for each
        # page-number and for each page-numbers following
        # that page-number, no rule stipulates that one of
        # succeeding page-numbers should precede the page-number
        # being checked; if that is the case, the update is
        # invalid; if there's no conflicting rule, the update
        # is valid
        update_valid = update_is_valid(update, rules, verbose=verbose)
        # if the current update is valid, bump the valid rules-counter
        # and add the middle element to the sum of middle elements
        if update_valid:
            n_valid_rules += 1
            valid_updates.append(update_index)
            verbose_msg(f"update[{update_index}]: OK", 2, verbose)
            if len_update % 2 != 1:
                # shouldn't get here
                print(f"len(update[{update_index}]) is even: BAD")
            else:
                sum_mid_valid += update[mid_index]
                sum_mid_all += update[mid_index]
                verbose_msg(f"mid = {update[mid_index]}\n", 2, verbose)
                verbose_msg(f"sum = {sum_mid_valid}", 2, verbose)
        else:
            all_updates_ok = False
            sum_mid_all += update[mid_index]
            invalid_updates.append(update_index)
            verbose_msg(f"update[{update_index}]: NOT ok", 2, verbose)
    if check_for_empty_rules(rules, verbose=verbose):
        # shouldn't get here
        verbose_msg("empty rules found", 1, verbose)
    else:
        verbose_msg("NO empty rules found", 1, verbose)
    verbose_msg(f"all_updates_ok = {all_updates_ok}", 1, verbose)
    verbose_msg(f"number of OK updates = {n_valid_rules}", 1, verbose)
    verbose_msg(f"sum of valid mid pages = {sum_mid_valid}", 0, verbose)
    verbose_msg(f"sum of all mid pages = {sum_mid_all}", 0, verbose)
    return updates, rules, sum_mid_valid


def part_2(updates, rules, first_sum, verbose: int = 0):
    """make invalid updates valid"""
    print("= " * 10)
    print(" PART 2")
    print("= " * 10)
    if not verify_updates(updates, rules, verbose=verbose):
        print("found invalid updates - fixing")
        fix_updates(updates, rules, verbose=verbose)
    if verify_updates(updates, rules, verbose=verbose):
        print("all updates now valid")
        for update in updates:
            verbose_msg(f"{update}", 1, verbose)
    second_sum = 0
    for update in updates:
        mid = int(len(update) / 2)
        second_sum += update[mid]
    print(f"sum of mids (valid updates) = {first_sum}")
    print(f"sum of mids (fixed updates) = {second_sum}")
    print(f"total sum = {second_sum + first_sum}")
    print(f"diff (the answer to part 2) = {second_sum - first_sum}")


def main():
    """main"""

    parser = argparse.ArgumentParser(description="aoc 2024 day 5",
                                     prog="day_5",
                                     add_help=True)
    parser.add_argument('--part', type=int, default=1,
                        choices=[1, 2],
                        help='part number (1 or 2)')
    parser.add_argument('--example', default=False,
                        action='store_true',
                        help='use example datafile')
    parser.add_argument('--verbose', type=int, default=0,
                        choices=[0, 1, 2],
                        help='get diagnostics')
    args = parser.parse_args()
    if args.part == 1:
        part_1(args.example, args.verbose)
    else:
        part_2(*part_1(args.example, args.verbose))


if __name__ == "__main__":
    main()
# vim: set numberwidth=4 number noignorecase :
