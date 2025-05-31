# pylint: disable=all
# coding: utf-8
import pandas as pd
# from .. helpers import __DATADIR__


def main():
    # df = pd.read_csv("data/day_4_part_2_data_example.csv", header=None)
    df = pd.read_csv("data/day_4_data.csv", header=None)
    n = len(df)
    count = 0
    for row in range(n):
        for col in range(n):
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
    #                    print(f"{df.iloc[row-1, col-1]} {df.iloc[row-1, col+1]}")
    #                    print(" A")
    #                    print(f"{df.iloc[row+1, col-1]} {df.iloc[row+1, col+1]}")
                except IndexError as e:
                    pass
    print(f"count = {count}")


if __name__ == "__main__":
    main()
