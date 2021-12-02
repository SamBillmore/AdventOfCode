from typing import List
import pandas as pd


def get_data(filepath: str) -> List:
    """ 
    """
    data_df = pd.read_csv(filepath, header=None)
    data_list = list(data_df.iloc[:, 0])
    return data_list
