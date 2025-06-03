"""
    get_input_file
        return path to datafile for day <daynum>, part <part>
"""

import os
import pathlib
import sys
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
    try:
        data_path = Path(sys.argv[1])
        if not os.access(data_path, os.R_OK):
            raise OSError
    except OSError as exception:
        raise SystemExit("No such file") from exception
    except IndexError:
        # Default data input
        default_path = f"{__DATADIR__}/day_{daynum}_part_{part}"
        if example:
            data_path = pathlib.Path(default_path + "_example_2")
        else:
            data_path = pathlib.Path(default_path)
    return data_path
