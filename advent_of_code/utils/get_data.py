from typing import List
import numpy as np
import pandas as pd


def get_csv_data(filepath: str) -> pd.DataFrame:
    """ 
    """
    return pd.read_csv(filepath, header=None)


def get_binary_data(filepath: str) -> List:
    """ 
    """
    byte_list = []
    with open(file=filepath, mode="rb") as f:  # b is important -> binary
        while (byte := f.read(13)):
            byte_list.append(byte[:12])
    return byte_list


def get_data_from_txt(filepath: str) -> List:
    """ 
    """
    return list(np.loadtxt(filepath, delimiter='\n', skiprows=0, dtype=str))
