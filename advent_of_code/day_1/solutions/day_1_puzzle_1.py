from typing import List
import pandas as pd
from advent_of_code.utils.get_data import get_csv_data


def data_munging(input_data: pd.DataFrame) -> List:
    """
    """
    return list(input_data.iloc[:, 0])


def count_depth_increase_from_previous_measurement(list_of_measurements: List) -> int:
    """ 
    """
    previous_measurement = None
    count = 0
    for measurement in list_of_measurements:
        if previous_measurement != None:
            if measurement > previous_measurement:
                count += 1
        previous_measurement = measurement
    return count


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_1_data.csv"
    input_data = get_csv_data(filepath)
    list_of_measurements = data_munging(input_data)
    count_increase = count_depth_increase_from_previous_measurement(list_of_measurements)
    print(f"Number of depth increases: {count_increase}")
