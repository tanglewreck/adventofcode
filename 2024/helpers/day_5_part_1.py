# coding: utf-8
"""check rules"""

import pathlib
from pathlib import Path, PosixPath
from collections import defaultdict

UPDATES = [
    [75, 47, 61, 53, 29],
    [97, 61, 53, 29, 13],
    [75, 29, 13],
    [75, 97, 47, 61, 53],
    [61, 13, 29],
    [97, 13, 75, 29, 47]
]

RULES_EXAMPLE = """47:53
97:13
97:61
97:47
75:29
61:13
75:53
29:13
97:29
53:29
61:53
97:53
61:29
47:13
75:47
97:75
47:61
75:61
47:29
75:13
53:13
"""

DEFAULT_DATA = pathlib.Path("data/day_5_part_1")


def get_data(data_file: Path | PosixPath = DEFAULT_DATA) -> tuple[dict, list]:
    """
        get_data()
            Read rules and updates from disk
    """
    with open(data_file) as fp:
        # get rule
        rules: dict[int, list[int]] = {}
        pos = 0
        while line := fp.readline().strip():
            if "XX" in line:
                break
            pre, post = map(int, line.split("|"))
    #        print(line, pre, post)
            if pre in rules:
                rules[pre].append(post)
            else:
                rules[pre] = [post]
            pos += 1
        pos += 1
        # read updates
        updates: list[list[int]] = []
        while line := fp.readline().strip():
            update = list(map(int, line.split(',')))
            updates.append(update)
            pos += 1
        # Added rules for all pages that's in
        # some update
        for update in updates:
            for page in update:
                if page not in rules:
                    rules[page] = []
    # print(updates)
    # [(k, " ".join([str(x) for x in v])) for k, v in rules.items()]
    # print(len(rules))
    return rules, updates


def build_rules():
    """build rules"""
    rules_list = RULES_EXAMPLE.split("\n")
    # rules = defaultdict()
    rules: dict[int, list] = {}
    # rules = {}
    # make a rule for all values in UPDATES,
    # so we can check if there's a rule for
    # every update entry
    for update in UPDATES:
        for u in update:
            if u not in rules:
                rules[u] = []
    # populate the rules dict
    for rule in [x.split(":") for x in rules_list][:-1]:
        # print(rule[0], rule[1])
        rule_key = int(rule[0])
        rule_val = int(rule[1])
        if rule_key not in rules:
            rules[rule_key] = [rule_val]
        else:
            rules[rule_key].append(rule_val)
    return rules


def main():
    """main"""
    verbose = 1
    rules, updates = get_data()
#     print("rules:")
#     print(rules)
#     print()
#     print()
#     print("updates")
#     print(updates)
#     for rulenum, rulelist in rules.items():
#         if not rulelist:
#             print(f"rule {rulenum} is empty ({rulelist})")
    # rules = build_rules()
    # print(f"rules: {rules}")
    all_ok = True
    # n_updates = len(updates)
    n_ok = 0
    # for k, update in enumerate(UPDATES[3:n_updates+1]):
    for k, update in enumerate(updates):
        update_ok = True
        if verbose > 0:
            print(f"update[{k}]: {update}")
        for i, u in enumerate(update):
            n = len(update)
            for j in update[i+1:n]:
                ok = j in rules[u]
                if verbose > 1:
                    print(f"{j} in rules[{u}] = {ok}")
                if not ok:
                    all_ok = False
                    update_ok = False
        if update_ok:
            n_ok += 1
            print(f"update[{k}]: OK")
        else:
            print(f"update[{k}]: NOT ok")
        # print()
    print(f"all_ok = {all_ok}")
    print(f"number of OK updates = {n_ok}")


if __name__ == "__main__":
    main()
