"""
    utils package
        contains modules commonly used by the
        'day_<n_day>[_part_<n_part>].py programs'
"""

from typing import NewType
from pandas import DataFrame
from . as_dataframe import as_dataframe
from . export_data import export_data
from . import_data import import_data
from . get_data_path import get_data_path
from . verbose_msg import verbose_msg
from . data_handler import DataHandler
from . __settings__ import __DATADIR__
from . __settings__ import __PREFIX__
from . __settings__ import __DATA_PREFIX__
# from . data_handler import DataHandler as dh

__version__ = "2025.06.07_01"
__author__ = "mier"

ImportDataList = NewType("ImportDataList", list[list[int]])
ImportDataDf = NewType("ImportDataDf", DataFrame)

__all__ = ["__version__",
           "__author__",
           "__PREFIX__",
           "__DATADIR__",
           "__DATA_PREFIX__",
           "DataHandler",
           "as_dataframe",
           "export_data",
           "get_data_path",
           "import_data",
           "verbose_msg"]
