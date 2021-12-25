from typing import List
from statistics import median

from advent_of_code.utils.get_data import get_csv_data_single_row


def find_horizontal_position(input_data: List) -> int:
    """
    """
    return int(median(input_data))


def calculate_fuel(input_data: List, horizontal_position: int) -> int:
    """
    """
    fuel_used = 0
    for position in input_data:
        fuel_used = fuel_used + abs(position -  horizontal_position)
    return fuel_used


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_7_data.csv"
    crab_data = get_csv_data_single_row(filepath)
    horizontal_position = find_horizontal_position(crab_data)
    output = calculate_fuel(crab_data, horizontal_position)
    print(f"Final output: {output}")
