"""
    export_data
"""
from pathlib import Path
import pandas as pd
from utils.get_data_path import get_data_path


def export_data(df: pd.DataFrame, daynum: int, part: int = 1, example=False) -> None:
    """
        export_data
            Sort and export a dataframe to a
            comma-separated (csv) file.
    """
    data_path: Path = get_data_path(daynum=daynum, part=part, example=example)
    try:
        df.to_csv(data_path, sep=",", index=False)
    except (OSError, pd.errors.ParserError) as e:
        print(repr(e))
