# coding: utf-8
"""
    diagonals
"""
from typing import List

# DATA =  ['MMMS', 'MSAM', 'AMXS', 'MSAM']
DATA =  ['ABCD', 'EFGH', 'IJKL', 'MNOP']

def diagonals(data: List[str], row: int = 0, verbose: int = 0) -> List[str]:
    """
        Return all diagonals that can be formed from
        a row of a dataset.
    """
    # Starting at the last column (c) of the row (r):
    #     - add data[r][c]
    #     - go to the next row (r += 1) and
    #       add the element to the right (c += 1) of
    #       the element of the last column, i.e. add
    #       data[r+1][c+1]
    #     - repeat until IndexError, i.e. until there
    #       are no more columns to the right of the
    #       first element added
    #     - add the diagonal formed by the above procedure
    #       to the list of diagonals
    # When we have reached the start of the row (data[row, 0]),
    nc: int = len(data[0])
    nr: int = len(data)
    if verbose:
        print(f"nr = {nr}, nc = {nc}")
    all_diagonals: List = []
    # Start at the last column of the row
    for col in range (nc-1, -1, -1):
        # Assign that element to the current diagonal
        # cur_diag = [data[row][col]]
        cur_diag = []
        try:
            # Starting from this row,
            # process every row below
            for r in range(row, nr):
                # Starting at the current column,
                # to the end of the current row...
                for c in range(col, nc + 1):
                    # Append to the current diagonal
                    cur_diag.append(data[row + r][r + c])
        except IndexError:
            # When done with the current diagonal,
            # add it to the list of all diagonals
            all_diagonals.append(cur_diag)
            continue
    return all_diagonals


def main():
    """main()"""
    data = DATA
    for d in data:
        print(d)
    out = diagonals(data, 0)
    print(out)


if __name__ == "__main__":
    main()
