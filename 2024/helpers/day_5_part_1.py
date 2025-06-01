# coding: utf-8
"""check rules"""

from collections import defaultdict


UPDATES = [
    [75, 47, 61, 53, 29],
    [97, 61, 53, 29, 13],
    [75, 29, 13],
    [75,97,47, 61, 53],
    [61, 13, 29],
    [97, 13, 75, 29, 47]
]

RULES_STR = """47:53
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

def build_rules():
    """build rules"""
    rules_list = RULES_STR.split("\n")
    rules = defaultdict()
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
    rules = build_rules()
    print(f"rules: {rules}")
    all_ok = True
    # n_updates = len(UPDATES)
    # for k, update in enumerate(UPDATES[3:n_updates+1]):
    for k, update in enumerate(UPDATES):
        update_ok = True
        print(f"update[{k}]: {update}")
        for i, u in enumerate(update):
            n = len(update)
            for j in update[i+1:n]:
                ok = j in rules[u]
                print(f"{j} in rules[{u}] = {ok}")
                if not ok:
                    all_ok = False
                    update_ok = False
        if update_ok:
            print(f"update[{k}]: OK")
        else:
            print(f"update[{k}]: NOT ok")
        print()
    print(f"all_ok = {all_ok}")


if __name__ == "__main__":
    main()
