# coding: utf-8
""" verify_updates """

from typing import DefaultDict, List
from utils.verbose_msg import verbose_msg
from . day_5_valid import update_is_valid


def verify_updates(updates: List[List[int]],
                   rules: DefaultDict[int, List[int]],
                   verbose: int = 0) -> bool:
    """
        verify_updates()
            verify that all updates are valid
    """
    all_valid = True
    for k, update in enumerate(updates):
        if not update_is_valid(update, rules):
            verbose_msg(f"update[{k}] not valid", 1, verbose)
            all_valid = False
        verbose_msg(f"update[{k}] is valid", 1, verbose)
    return all_valid
