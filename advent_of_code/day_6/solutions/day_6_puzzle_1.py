from typing import List
import pandas as pd
from advent_of_code.utils.get_data import get_csv_data_single_row


def single_fish_iteration(munged_data: List) -> List:
    """
    """
    current_fish = []
    additional_fish = []
    for fish in munged_data:
        if fish == 0:
            current_fish.append(6)
            additional_fish.append(8)
        else:
            current_fish.append(fish - 1)
    return current_fish + additional_fish


def iterate_fish(fish_data: List, iterations: int) -> List:
    """
    """
    for _ in range(0,iterations,1):
        fish_data = single_fish_iteration(fish_data)
    return fish_data


def count_fish(fish_data: List) -> int:
    """
    """
    return len(fish_data)


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_6_data.csv"
    fish_data = get_csv_data_single_row(filepath)
    fish_data = iterate_fish(fish_data, iterations=80)
    output = count_fish(fish_data)
    print(f"Final output: {output}")
