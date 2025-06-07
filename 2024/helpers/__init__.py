"""__init__"""

import os
from . day_4_count_matches import count_matches
from . day_4_xmas import x_mas_np, x_mas_pd, x_mas_list
from . day_4_xmas_count import count_xmas

__version__ = "0.1.4"
__author__ = "mier"
__name__ = "helpers"  # pylint: disable=redefined-builtin

__BASEDIR__ = f"{os.environ['HOME']}/Proj/adventofcode/2024"
__DATADIR__ = f"{__BASEDIR__}/data"  # data directory path

__all__ = ["__BASEDIR__",
           "__DATADIR__",
           "count_matches",
           "count_xmas",
           "x_mas_np",
           "x_mas_pd",
           "x_mas_list"
           ]
