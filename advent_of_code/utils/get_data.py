from typing import List
import numpy as np
import pandas as pd


def get_csv_data(filepath: str) -> List:
    """ 
    """
    data_df = pd.read_csv(filepath, header=None)
    data_list = list(data_df.iloc[:, 0])
    return data_list


def get_binary_data(filepath: str):
    """ 
    """
    byte_list = []
    with open(file=filepath, mode="rb") as f:  # b is important -> binary
        while (byte := f.read(13)):
            byte_list.append(byte[:12])
    return byte_list


def get_data_from_txt(filepath: str):
    """ 
    """
    return list(np.loadtxt(filepath, delimiter='\n', skiprows=0, dtype=str))
