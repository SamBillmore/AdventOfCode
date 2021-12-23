from typing import List

from advent_of_code.utils.get_data import get_csv_data
from advent_of_code.day_1.solutions.day_1_puzzle_1 import data_munging


def three_measurement_windows(list_of_measurements: List) -> int:
    """ 
    """
    first_previous_measurement = None
    second_previous_measurement = None
    previous_combined_measurement = None
    combined_measurement = None
    count = 0
    for measurement in list_of_measurements:
        if second_previous_measurement != None:
            combined_measurement = measurement + first_previous_measurement + second_previous_measurement
            if previous_combined_measurement != None:
                if combined_measurement > previous_combined_measurement:
                    count += 1
        second_previous_measurement = first_previous_measurement
        first_previous_measurement = measurement
        previous_combined_measurement = combined_measurement
    return count


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_1_data.csv"
    input_data = get_csv_data(filepath)
    list_of_measurements = data_munging(input_data)
    count_increase = three_measurement_windows(list_of_measurements)
    print(f"Number of depth increases: {count_increase}")
