"""
    utils package
        contains modules commonly used by the
        'day_<n_day>[_part_<n_part>].py programs'
"""

import os
import imp

__version__ = "0.5.1"
__author__ = "mier"
__name__ = "utils"  # pylint: disable=redefined-builtin

__BASEDIR__ = f"{os.environ['HOME']}/Proj/adventofcode/2024"
__DATADIR__ = f"{__BASEDIR__}/data"  # data directory path

__all__ = ["__BASEDIR__", "__DATADIR__"]
