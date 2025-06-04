"""
    get_input_file
        return path to datafile for day <daynum>, part <part>
"""

import os
import pathlib
from pathlib import Path
from helpers import __DATADIR__


def get_data_path(daynum: int, part: int, example: bool = False) -> Path:
    """
        get_data_path
            return path to datafile for day <daynum>, part <part>
    """
    #
    # import argparse
    #
    # Check for a commandline argument and use that as
    # the path to the file containing the input data
    # Default data input
    data_path = Path(f"{__DATADIR__}/day_{daynum}_part_{part}")
    try:
        if example:
            data_path = pathlib.Path(str(data_path) + "_example")
        else:
            data_path = pathlib.Path(data_path)
        if not os.access(data_path, os.R_OK):
            raise OSError
    except OSError as exception:
        raise SystemExit(2, f"{__name__}: No such file: {data_path}") from exception
    return data_path
