"""__init__"""

import os

__version__ = "0.1.4"
__author__ = "mier"
__name__ = "helpers"  # pylint: disable=redefined-builtin

__BASEDIR__ = f"{os.environ['HOME']}/Proj/adventofcode/2024"
__DATADIR__ = f"{__BASEDIR__}/data"  # data directory path

__all__ = ["__BASEDIR__", "__DATADIR__"]
