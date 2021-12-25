from typing import List

from advent_of_code.utils.get_data import get_csv_data_single_row


def calculate_fuel_2(input_data: List, horizontal_position: int) -> int:
    """
    """
    total_fuel_used = 0
    for position in input_data:
        fuel_used = _calculate_triangle_number(abs(position - horizontal_position))
        total_fuel_used = total_fuel_used + fuel_used
    return total_fuel_used


def _calculate_triangle_number(input_number: int) -> int:
    """
    """
    output = 0
    for i in range(0,input_number):
        output = output + i + 1
    return output


def find_position(input_data: List) -> int:
    """
    """
    pass


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_7_data.csv"
    crab_data = get_csv_data_single_row(filepath)
    output = find_position(crab_data)
    print(f"Final output: {output}")
