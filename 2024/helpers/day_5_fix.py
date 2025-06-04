# coding: utf-8
""" fix_update """

from typing import DefaultDict, List
from utils.verbose_msg import verbose_msg
from .day_5_switch import switch
from .day_5_valid import update_is_valid


def fix_update(update: List[int],
               rules: DefaultDict[int, List[int]],
               verbose: int = 0) -> bool:
    """
        fix_update()
            fix an update according to the rules
            returns True if the update was correctly corrected,
            otherwise False
    """
    if update_is_valid(update, rules):
        verbose_msg(f"update ({update}) is already valid", 1, verbose)
        return True
    verbose_msg("= = = = = = = = = = = = = = = = = = = =\n"
                f"PRE: {update} not valid:\n"
                "= = = = = = = = = = = = = = = = = = = =", 1, verbose)
    n = len(update)
    for i in range(n):
        verbose_msg(f"\t- - - - {'- - ' * (len(update) - 1)}-", 1, verbose)
        verbose_msg(f"\tpre: {update}", 1, verbose)
        verbose_msg(f"\t- - - - {'- - ' * (len(update) - 1)}-", 1, verbose)
        for j in range(i, n):
            verbose_msg(f"\tchecking {i} ({update[i]}) against {j} "
                        f"({update[j]}): {update[i]} in r({update[j]})",
                        1, verbose)
            if update[i] in rules[update[j]]:
                switch(update, i, j)
                verbose_msg(f"\t\t(switching {update[i]} <--> {update[j]})",
                            1, verbose)
            verbose_msg(f"\tupdate is now {update}\n", 1, verbose)
    if update_is_valid(update, rules):
        verbose_msg(f"update ({update}) is valid"
                    f"({update_is_valid(update, rules)})",
                    1, verbose)
    else:
        verbose_msg(f"update ({update}) is NOT valid"
                    f"({update_is_valid(update, rules)})",
                    1, verbose)
    return update_is_valid(update, rules)


def fix_updates(updates: List[List[int]],
                rules: DefaultDict[int, List[int]],
                verbose: int = 0) -> None:
    """
        fix_updates()
            correct all updates according to the rules
    """
    for update in updates:
        fix_update(update, rules, verbose=verbose)
