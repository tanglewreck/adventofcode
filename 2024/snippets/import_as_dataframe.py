"""import_as_dataframe"""

import re
from typing import List, Optional
import pandas as pd

__all__ = ["import_as_dataframe"]
__version__ = "0.4.1"
__author__ = "mier"
__date__ = "2025-05-30"

# pylint: disable=unused-variable
FULL_DATA = "data/day_4_data"
FULL_DATA_CSV = "data/day_4_data.csv"
EXAMPLE_DATA = "data/day_4_data_example"
EXAMPLE_DATA_CSV = "data/day_4_data_example.csv"
# pylint: enable=unused-variable


def import_as_dataframe(path: str = EXAMPLE_DATA,
                        save: bool = False,
                        verbose: int = 0) -> Optional[pd.DataFrame]:
    """import and optionally save as csv"""
    try:
        with open(path, encoding="utf-8") as fp:
            # Collect rows as a list of type List[List[str]]
            rows: List[List[str]] = [re.split(r'', row.strip())[1:-1]
                                     for row in fp.readlines()]
            if verbose:
                print(f"rows: {rows}")
            if verbose > 0:
                print(f"Rows read: {rows}")
            # Save to file if asked to
            if save:
                outpath = path + ".csv"
                # transform rows to List[str] (each string ending with "\n")
                outrows: List[str] = [",".join(row) + "\n" for row in rows]
                if verbose > 0:
                    print(f"saving data from {path} to csv-file {outpath}")
                with open(outpath, "w", encoding="utf-8") as fp_out:
                    fp_out.writelines(outrows)
            return pd.DataFrame(rows)
    except OSError as exception:
        print(repr(exception))
        return None
    return None
