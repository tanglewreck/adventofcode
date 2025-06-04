"""
    import_data
"""
from pathlib import Path
import pandas as pd
from utils.get_data_path import get_data_path

__all__: list[str] = ["import_data"]


def import_data(daynum: int, part: int = 1, example=False) -> pd.DataFrame:
    """
        import_data
            - Reads a comma-separated datafile.
            - Returns a pandas.DataFrame, dtype=int,
              with NaN's replaced by zeroes.
            - The file should be named "day_<n>_data[_example]",
              where n is an integer and the '_example' suffix
              is optional.
    """
    data_path: Path = get_data_path(daynum, part=part, example=example)
    try:
        with open(data_path) as fp:
            temp_df = pd.read_csv(fp, sep=",", dtype=float)
            # Replace NaN's with 0.0
            temp_df.fillna(0.0, inplace=True)
            # Convert to int
            temp_df = temp_df.astype(int)
            # temp_df.to_csv(fname + "_padded", sep=",", index=None)
            return temp_df
    except (OSError, pd.errors.ParserError) as exception:
        print(repr(exception))
        raise SystemExit(1, repr(exception)) from exception
