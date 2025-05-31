# pylint: disable=all
# coding: utf-8
import pandas as pd
import numpy as np
# from .. helpers import __DATADIR__


def main():
    df4e = pd.read_csv("data/day_4_part_2_data_example.csv", header=None)
    df4f = pd.read_csv("data/day_4_data.csv", header=None)
    df = df4e
    df = df4f
    n = len(df)
    count = 0
    for row in range(n):
        for col in range(n):
            if row == 0 or row == n-1 or col == 0 or col == n-1:
                continue
            if df.iloc[row, col] == 'A':
                try:
                    if ((df.iloc[row-1, col-1] == "M" and df.iloc[row-1, col+1] == "S") and
                        (df.iloc[row+1, col-1] == "M" and df.iloc[row+1, col+1] == "S")):
                        count += 1
                    if ((df.iloc[row-1, col-1] == "M" and df.iloc[row-1, col+1] == "M") and
                        (df.iloc[row+1, col-1] == "S" and df.iloc[row+1, col+1] == "S")):
                        count += 1
                    if ((df.iloc[row-1, col-1] == "S" and df.iloc[row-1, col+1] == "S") and
                        (df.iloc[row+1, col-1] == "M" and df.iloc[row+1, col+1] == "M")):
                        count += 1
                    if ((df.iloc[row-1, col-1] == "S" and df.iloc[row-1, col+1] == "M") and
                        (df.iloc[row+1, col-1] == "S" and df.iloc[row+1, col+1] == "M")):
                        count += 1
                except IndexError as e:
                    pass
    print(f"count = {count}")

    rows_full = np.asarray(df4f)
    rows_example = np.asarray(df4e)
    rows = rows_example
    rows = rows_full
    n = len(rows)
    count = 0
    for row in range(n):
        for col in range(n):
            if row == 0 or row == n-1 or col == 0 or col == n-1:
                continue
            if rows[row][col] == 'A':
                if ((rows[row-1][col-1] == 'M' and rows[row-1][col+1] == 'M') and
                    (rows[row+1][col-1] == 'S' and rows[row+1][col+1] == 'S')):
                    count += 1
                if ((rows[row-1][col-1] == 'M' and rows[row-1][col+1] == 'S') and
                    (rows[row+1][col-1] == 'M' and rows[row+1][col+1] == 'S')):            
                    count += 1 
                if ((rows[row-1][col-1] == 'S' and rows[row-1][col+1] == 'M') and
                    (rows[row+1][col-1] == 'S' and rows[row+1][col+1] == 'M')):
                    count += 1
                if ((rows[row-1][col-1] == 'S' and rows[row-1][col+1] == 'S') and            
                    (rows[row+1][col-1] == 'M' and rows[row+1][col+1] == 'M')):
                    count += 1            
    print(f"count = {count}")

    rows_full = [list(row) for row in np.asarray(df4f)]
    rows_example = [list(row) for row in np.asarray(df4e)]
    rows = rows_example
    rows = rows_full
    n = len(rows)
    count = 0
    for row in range(1, n-1):
        for col in range(1, n-1):
            if rows[row][col] == 'A':
                if ((rows[row-1][col-1] == 'M' and rows[row-1][col+1] == 'M') and
                    (rows[row+1][col-1] == 'S' and rows[row+1][col+1] == 'S')):
                    count += 1
                if ((rows[row-1][col-1] == 'M' and rows[row-1][col+1] == 'S') and
                    (rows[row+1][col-1] == 'M' and rows[row+1][col+1] == 'S')):            
                    count += 1 
                if ((rows[row-1][col-1] == 'S' and rows[row-1][col+1] == 'M') and
                    (rows[row+1][col-1] == 'S' and rows[row+1][col+1] == 'M')):
                    count += 1
                if ((rows[row-1][col-1] == 'S' and rows[row-1][col+1] == 'S') and            
                    (rows[row+1][col-1] == 'M' and rows[row+1][col+1] == 'M')):
                    count += 1            
    print(f"count = {count}")

if __name__ == "__main__":
    main()
