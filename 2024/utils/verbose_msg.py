"""
    verbose_msg
"""


def verbose_msg(msg: str, verbose_lvl_req: int, verbose_lvl: int = 0):
    """print msg if verbose level is high enough"""
    if verbose_lvl >= verbose_lvl_req:
        print(msg)
