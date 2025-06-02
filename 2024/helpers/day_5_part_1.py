# coding: utf-8
"""check rules"""

from pathlib import Path
from collections import defaultdict

DEFAULT_DATA = Path("data/day_5_part_1")


def get_data(data_file: Path = DEFAULT_DATA, verbose=0) -> tuple[dict, list]:
    """
        get_data()
            Read rules and updates from disk
    """
    with open(data_file) as fp:
        # rules are stored in a dictionary with page-numbers
        # as keys and a list of all pages that cannot preceed
        # the key-page as values:
        #   <page that must come befor>: [<pages that must follow>]
        #
        # initialise the rules dict as a collections.defaultdict that
        # sets the dict-value to an empty list, if there's not already
        # a key for that value, and then appends the value to that list
        # rules: dict[int, list[int]] = {}
        rules: defaultdict[int, list[int]] = defaultdict(lambda: [])
        # read rules until the rules-updates separator
        # "XX" is encounterd
        while line := fp.readline().strip():
            # if we have encountered the separator,
            # we're done reading rules
            if "XX" in line:
                break
            # break up the rule; split on "|" and
            # convert each part to an int
            pre, post = map(int, line.split("|"))
            if verbose > 1:
                print(line, pre, post)
            # if there's a rule already, append to it;
            # otherwise initialise the rule with an empty list
            rules[pre].append(post)  # type(rules) = collections.defaultdict!
        # read updates
        updates: list[list[int]] = []
        while line := fp.readline().strip():
            update = list(map(int, line.split(',')))
            updates.append(update)
        # Add rules for all pages that's in at least one update
        for update in updates:
            for page in update:
                if page not in rules:
                    rules[page] = []
    # print(updates)
    # print([(k, " ".join([str(x) for x in v])) for k, v in rules.items()])
    if verbose:
        print(rules)
        print(f"there are {len(rules)} rules")
    return rules, updates
