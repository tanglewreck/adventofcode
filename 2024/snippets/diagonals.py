"""import_as_dataframe"""

from typing import List
import numpy as np
import pandas as pd

__all__ = ["diagonals"]
__version__ = "0.4.1"
__author__ = "mier"
__date__ = "2025-05-30"


def diagonals(df_in: pd.DataFrame, verbose: int = 0) -> List[str]:
    """Extract diagonals from a dataframe"""
    # Convert to np.ndarray so that we can use
    # np.diagonal() to extract diagonals (make
    # a copy so the input dataframe is not affected).
    df = np.asarray(df_in.copy())
    # Flip data left-to-right, i.e. reverse/mirror rows
    df_flipped = np.fliplr(df)
    n = len(df)
    diags: list = [df[row_col:n, :(n - row_col)].diagonal()
                   for row_col in range(n)]
    diags_flipped: list = [df_flipped[row_col:n, :(n - row_col)].diagonal()
                           for row_col in range(n)]
    if verbose > 1:
        print(f"diagonals: {diags}")
        print(f"diagonals (flipped df): {diags_flipped}")
    return diags + diags_flipped
