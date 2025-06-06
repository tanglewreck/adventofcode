"""
    get_input_file
        return path to datafile for day <day>, part <part>
"""

import os
import pathlib
# import re
from pathlib import Path
from typing import Iterable, List
import pandas as pd
from utils.__settings__ import __DATADIR__


class DataHandler:
    """
        DataHandler - oop version of utility routines
    """
    @staticmethod
    def get_data_path(day: int, part: int, example: bool = False) -> Path:
        """
            get_data_path
                return path to datafile for day <day>, part <part>
        """
        #
        # import argparse
        #
        # Check for a commandline argument and use that as
        # the path to the file containing the input data
        # Default data input
        data_path = Path(f"{__DATADIR__}/day_{day}_part_{part}")
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

    @staticmethod
    def import_data(day: int, part: int = 1, example=False, raw=False, dtype="int"):
        """
            import_data*
                either returns pd.DataFrame | List[str] (for raw data = as
                downloaded from adventofcode.com)
        """
        data_path: Path = DataHandler.get_data_path(day, part=part, example=example)
        if raw:
            # data: List[str] | List[List[int]] = []
            data: Iterable[List[int]] | List[str] = []
            data_path = DataHandler.get_data_path(day, part, example=example)
            data_path = Path(str(data_path) + "_raw")
            try:
                with open(data_path, 'r', encoding="UTF-8") as fp:
                    if dtype == "int":
                        # split lines:
                        #   lines are split on whitespace and then elements are cast
                        #   to integers; a list of lists of integers is the result
                        #   (shape = (n, m))
                        data = [[int(s) for s in line.split()]
                                for line in list(open(data_path))]
                        # cast to a pd.DataFrame
                        df = pd.DataFrame(data)
                        # Replace NaN's with 0.0
                        df.fillna(0.0, inplace=True)
                        # Convert to int
                        df = df.astype(int)
                        return df  # pd.DataFrame
                    if dtype == "str":
                        return fp.read()
                    # don't process (split, or otherwise) lines
                    data = list(fp)
                    return data  # Iterable[str]

            except OSError as exception:
                raise SystemExit(2, f"{__name__}: No such file: {data_path}") from exception
        # non-raw data = edited after download (i.e. converted to csv)
        try:
            with open(data_path) as fp:
                temp_df = pd.read_csv(fp, sep=",", dtype=float)
                # Replace NaN's with 0.0
                temp_df.fillna(0.0, inplace=True)
                # Convert to int
                temp_df = temp_df.astype(int)
                return temp_df
        except (OSError, pd.errors.ParserError) as exception:
            print(repr(exception))
            raise SystemExit(1, repr(exception)) from exception

    @staticmethod
    def export_data(df: pd.DataFrame, day: int, part: int = 1, example=False) -> None:
        """
            export_data:
                Sort and export a dataframe to a
                comma-separated (csv) file.
        """
        data_path: Path = DataHandler.get_data_path(day, part, example=example)
        try:
            df.to_csv(data_path, sep=",", index=False)
        except (OSError, pd.errors.ParserError) as e:
            print(repr(e))
