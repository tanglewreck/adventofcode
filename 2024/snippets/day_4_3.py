# coding: utf-8
""" stuff """

# pylint: disable=too-many-locals

import re
import numpy as np
import pandas as pd

DF = pd.read_csv("data/day_4_data_example.csv", header=None)
N = len(DF)

def diagonals(df: pd.DataFrame = DF, start: int = 4, stop: int = N, verbose: int = 0):
    """Extract diagonals from a dataframe"""
    # convert to np.ndarray:s
    data = np.asarray(df.copy())
    data_rev = np.fliplr(data)
    # Initialise lists that will hold
    # partitions of the data
    partitions = []
    partitions_rev = []
    # Initialise lists that will hold
    # diagonals extracted from the partitions
    diags = []
    diags_rev = []
    # Go from the top row's left and right corners,
    # respectively, and extract successively larger
    # k by k-sized partitions
    # stop = len(df)
    n = len(df)
    for r in range(start, stop + 1):
        try:
            # Counting from the top-left corner for
            # both data sets (the original and the
            # mirrored/rev)
            partition1 = np.asarray(data[:r, :r])
            partition1_rev = np.asarray(data_rev[:r, :r])
            # Likewise, but now starting at the top-right corner
            partition2 = np.asarray(data[:r, n - r:])
            partition2_rev = np.asarray(data_rev[:r, n - r:])
            # Collect/append
            partitions.append(partition1)
            partitions.append(partition2)
            partitions_rev.append(partition1_rev)
            partitions_rev.append(partition2_rev)
            # Extract diagonals
            diag1 = partition1.diagonal()
            diag2 = partition2.diagonal()
            diag1_rev = partition1_rev.diagonal()
            diag2_rev = partition2_rev.diagonal()
            diags.append(diag1)
            diags.append(diag2)
            diags_rev.append(diag1_rev)
            diags_rev.append(diag2_rev)
            # Print some diagnostics
            if verbose > 1:
                print(r, diag1)
                print(r, diag2)
                print(r, diag1_rev)
                print(r, diag2_rev)
                print()
        except IndexError:
            print("SHOULD NOT GET HERE")
    # Return diagonals
    return diags + diags_rev


def n_xmas_rows(df: pd.DataFrame = DF, verbose: int = 0):
    """
        Count the number of times 'XMAS' occurs in columns
    """
    n_xmas = 0
    k = 0
    n = len(df)
    for row in range(n):
        row_string = "".join(df.iloc[row])
        if 'XMAS' in row_string or 'SAMX' in row_string:
            matches = re.findall(r'XMAS', row_string)
            matches_rev = re.findall(r'SAMX', row_string)
            n_xmas += len(matches) + len(matches_rev)
            if verbose > 0:
                print(f"'XMAS'/'SAMX' found in row {k}\t{row_string}")
        k += 1
        if verbose > 0:
            print(f"Number of 'XMAS' in rows = {n_xmas}")
    return n_xmas



def n_xmas_cols(df: pd.DataFrame = DF, verbose: int = 0):
    """
        Count the number of times 'XMAS' occurs in columns
    """
    n_xmas = 0
    k = 0
    n = len(df)
    for col in range(n):
        col_string = "".join(df.iloc[:, col])
        if 'XMAS' in col_string or 'SAMX' in col_string:
            matches = re.findall(r'XMAS', col_string)
            matches_rev = re.findall(r'SAMX', col_string)
            n_xmas += len(matches) + len(matches_rev)
            if verbose > 0:
                print(f"'XMAS'/'SAMX' found in row {k}\t{col_string}")
        k += 1
        if verbose > 0:
            print(f"Number of 'XMAS' in columns = {n_xmas}")
    return n_xmas



def n_xmas_diags(df: pd.DataFrame = DF, verbose: int = 0) -> int:
    """
        Count the number of times 'XMAS' occurs in diagonals
    """
    # Extract diagonals
    diags = diagonals(df, 0, len(df) + 1, verbose=0)
    print([list(diag) for diag in diags])
    # Initialise counter
    n_xmas = 0
    # Loop through the list of diagonals extracted from
    # the dataframe and check if 'XMAS', 'SAMX', or both
    # occur there.
    for k, diag in enumerate(diags):
        # Convert to string
        diag_string = "".join(diag)
        diag_string_rev = diag_string[::-1]
        if verbose > 0:
            print(f"diag_string = {diag_string}")
            print(f"diag_string_rev = {diag_string_rev}")
        # If we get a hit, up the counter
        if 'XMAS' in diag_string or 'SAMX' in diag_string:
            matches = re.findall(r'XMAS', diag_string)
            matches_rev = re.findall(r'SAMX', diag_string)
            n_xmas += len(matches) + len(matches_rev)
            if verbose > 0:
                print(f"'XMAS'/'SAMX' in diag {k}\t{diag_string}")
        k += 1
        if verbose > 0:
            print(f"Number of 'XMAS'/'SAMX' in diagonals = {n_xmas}")
    return n_xmas
