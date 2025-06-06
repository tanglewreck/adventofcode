"""
    __settings__
"""
import os

__BASEDIR__ = f"{os.environ['HOME']}/Proj/adventofcode/2024"
__DATADIR__ = f"{__BASEDIR__}/data"  # data directory path
__PREFIX__ = "day"
__DATA_PREFIX__ = __PREFIX__

__all__ = ["__PREFIX__",
           "__DATADIR__",
           "__DATA_PREFIX__"
           ]
