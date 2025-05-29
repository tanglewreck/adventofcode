# coding: utf-8
"""
    Extract diagonals:
        - downwards, going left-to-right
        - downwards, going right-to-left
"""

import numpy as np
import pandas as pd

DF = pd.read_csv("data/day_4_data_example.csv", header=None)
N = len(DF)


def extract_diagonals(df):
    """Extract diagonals from a dataframe"""

    def lower_left_diagonals(df, start=-1, stop=-1):
        """Extract upper-left diagonals (going left to right)"""
        d = np.asarray(df)
        n = len(d)
        if start == -1:
            start = len(df) - 4
        diags = []
        for row in range(start, stop, -1):
            diag = d[row:n, :n - row].diagonal()
            diags.append(diag)
        return diags

    def upper_right_diagonals(df, start=4, stop=0):
        """Extract lower-right diagonals (going left to right)"""
        d = np.asarray(df)
        # if start == 0:
        #    start = 4
        if stop == 0:
            stop = len(df)
        diags = []
        for k in range(start, stop):
            diag = np.fliplr(np.fliplr(d)[:k, :k]).diagonal()
            diags.append(diag)
        return diags

    def upper_left_diagonals(df, start=4, stop=0):
        """Extract lower-right diagonals (going left to right)"""
        d = np.asarray(df)
        if stop == 0:
            stop = len(df)
        diags = []
        for k in range(start, stop):
            diag = d[:k, :k][::-1].diagonal()[::-1]
            diags.append(diag)
        return diags

    diagonals = lower_left_diagonals(df, N - 1)
    diagonals += upper_right_diagonals(df, 1)
    diagonals += upper_left_diagonals(df, 1)

    return diagonals


def main():
    """main()"""
    diags = extract_diagonals(DF)
    for diag in diags:
        print(list(diag))
    print(len(diags))


if __name__ == "__main__":
    main()
