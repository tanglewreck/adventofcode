# coding: utf-8
""" foo  """
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=unused-variable
# pylint: disable=unused-argument
# pylint: disable=unused-import
# xpylint: disable=undefined-variable

import re
import typing
from typing import Optional
from typing import Tuple
import numpy as np
import pandas as pd

FULL_DATA_CSV = "data/day_4_data.csv"
EXAMPLE_DATA_CSV = "data/day_4_data_example.csv"


@typing.no_type_check
def import_data(path: str, verbose: int = 0) -> Tuple[str, str]:
    """Read data from file"""
    try:
        if verbose > 0:
            print(f"path = {path}")
        with open(path + "_example", encoding="utf-8") as fp:
            example_data = fp.read().strip()
        with open(path, encoding="utf-8") as fp:
            full_data= fp.read().strip()
        return (example_data, full_data)
# pylint: enable=unused-variable
    except OSError as exception:
        print(repr(exception))
        raise SystemExit(1) from exception


@typing.no_type_check
def import_as_dataframe(path: str, verbose: int = 0) -> Optional[pd.DataFrame]:
    """import and save as csv"""
    outpath = path + ".csv"
    if verbose > 0:
        print(outpath)
    try:
        with open(path, encoding="utf-8") as fp:
            rows = [re.split(r'', row.strip())[1:-1] for row in fp.readlines()]
            if verbose:
                print(f"rows: {rows}")
            # rows = [",".join(
            #    (re.split(r'', row.strip()))[1:-1]) + "\n"
            #        for row in fp.readlines()
            #]
            if verbose > 0:
                print(f"Rows read: {rows}")
            return pd.DataFrame(rows)
            #with open(outpath, "w", encoding="utf-8") as fp_out:
            #    fp_out.writelines(rows)
            # return pd.DataFrame()
    except OSError as exception:
        print(repr(exception))
        return None
        # raise SystemExit(1) from exception
    return None



@typing.no_type_check
def main():
    """main"""
    # Import data
    # example_data, full_data = import_data("../data/day_4_data")
    ed = example_data = import_as_dataframe("data/day_4_data_example")
    fd = full_data = import_as_dataframe("data/day_4_data")


if __name__ == "__main__":
    main()



#     # Data comes in the form of a string with
#     # embedded newlines (as read by read()).
#     # In order to make data easier to handle,
#     # begin by splitting on those newlines.
#     # example_data_split = example_data.split("\n")
#     # full_data_split = full_data.split("\n")
#     # Create less descriptive but definitely more
#     # manageable aliases for those
#
#     eds = example_data_split
#     fds = full_data_split
#     regexp = re.compile(r'(\w)')
#     ednp = [re.split(r'', row)[1:-1] for row in eds]
#     fdnp = [re.split(r'', row)[1:-1] for row in fds]
#
#     ednp = [re.findall(regexp, row) for row in eds]
#     fdnp = [re.findall(regexp, row) for row in fds]
#     d = []
#     for row in example_data.split("\n"):
#         d.append(re.findall(r'(\w)', row))
#     ednp = np.array(d)
#     d = []
#     for row in full_data.split("\n"):
#         d.append(re.findall(r'(\w)', row))
#     fdnp = np.array(d)
#
#     n_xmas = 0
#
#     regexp = re.compile(r'XMAS')
#     dnp = ednp
#     d = eds
#     n = len(dnp)
#     verbose = 1
#     for row_col in range(n - 1, -1, -1):
#         if verbose > 0:
#             print(f"row_col = {row_col}")
#         diag_1 = "".join(dnp[row_col:n, row_col:n].diagonal())
#         diag_1_rev = diag_1[::-1]
#         if verbose > 0:
#             print(f"diag_1 = {diag_1}")
#             print(f"diag_1_rev = {diag_1_rev}")
#         n = len(re.findall(regexp, diag_1))
#         nrev = len(re.findall(regexp, diag_1_rev))
#         n_xmas += len(re.findall(regexp, diag_1))
#         n_xmas += len(re.findall(regexp, diag_1_rev))
#
#         diag_2 = "".join(np.fliplr(dnp[row_col:n, row_col:n]).diagonal())
#         diag_2_rev = diag_2[::-1]
#         if verbose > 0:
#             print(f"diag_2 = {diag_2}")
#             print(f"diag_2_rev = {diag_2_rev}")
#         n_xmas += len(re.findall(regexp, diag_1))
#         n_xmas += len(re.findall(regexp, diag_1_rev))
#
#         row_str = d[row_col]
#         row_str_rev = row_str[::-1]
#         if verbose > 0:
#             print(f"row_str = {row_str}")
#             print(f"row_str_rev = {row_str_rev}")
#         n_xmas += len(re.findall(regexp, diag_1))
#         n_xmas += len(re.findall(regexp, diag_1_rev))
#
#         col_str = "".join(dnp[:, row_col])
#         col_str_rev = col_str[::-1]
#         if verbose > 0:
#             print(f"col_str = {col_str}")
#             print(f"col_str_rev = {col_str_rev}")
#         n_xmas += len(re.findall(regexp, diag_1))
#         n_xmas += len(re.findall(regexp, diag_1_rev))
#         if verbose > 0:
#             print()
#     print(f"n_xmas = {n_xmas}")
