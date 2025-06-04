"""
    utils package
        contains modules commonly used by the
        'day_<n_day>[_part_<n_part>].py programs'
"""

import os
from . as_dataframe import as_dataframe
from . export_data import export_data
from . import_data import import_data
from . get_data_path import get_data_path
from . verbose_msg import verbose_msg

__version__ = "0.5.1"
__author__ = "mier"
__name__ = "utils"  # pylint: disable=redefined-builtin

__BASEDIR__ = f"{os.environ['HOME']}/Proj/adventofcode/2024"
__DATADIR__ = f"{__BASEDIR__}/data"  # data directory path
__PREFIX__ = "day"

__all__ = ["__DATADIR__",
           "__PREFIX__",
           "as_dataframe",
           "export_data",
           "get_data_path",
           "import_data",
           "verbose_msg"]
