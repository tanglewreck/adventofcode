""" update_is_valid """

from typing import DefaultDict, List
from utils.verbose_msg import verbose_msg


def update_is_valid(update: List[int],
                    rules: DefaultDict[int, List[int]],
                    verbose: int = 0) -> bool:
    """
        update_is_valid
            check if a rule is valid according to the rules
    """
    update_valid: bool = True
    for cur_index, cur_item in enumerate(update):
        n = len(update)
        # check that the current item (page-number) does not occur
        # in any of the rules for the following page-numbers
        for post_item in update[cur_index + 1: n]:
            # if the current item does not occur in any rule for
            # the items that follow it, then we're good
            # ok = post_item in rules[cur_item]  # this one, or
            ok = cur_item not in rules[post_item]  # this one...
            verbose_msg(f"{post_item} in rules[{cur_item}] = {ok}",
                        verbose_lvl_req=2, verbose_lvl=verbose)
            if not ok:
                update_valid = False
    return update_valid
