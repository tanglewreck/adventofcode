"""
    __settings__
"""
import os
from dataclasses import dataclass

__BASEDIR__ = f"{os.environ['HOME']}/Proj/adventofcode/2024"
__DATADIR__ = f"{__BASEDIR__}/data"  # data directory path
__PREFIX__ = "day"
__DATA_PREFIX__ = __PREFIX__


# colours
@dataclass
class BColors:
    """ansi colours"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


__all__ = ["__PREFIX__",
           "__DATADIR__",
           "__DATA_PREFIX__",
           "BColors"
           ]
