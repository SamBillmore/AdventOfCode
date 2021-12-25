from typing import List
import math
import numpy as np

from advent_of_code.utils.get_data import get_csv_data_single_row


def iterate_fish_version_2(fish_data: List, iterations: int) -> List:
    """
    """
    # Set up blank data structure
    days_to_spawn_list = [0,0,0,0,0,0,0,0,0] # index indicates number of days left before spawning
    
    # Handle input data
    for fish in fish_data:
        days_to_spawn_list[fish] = days_to_spawn_list[fish] + 1

    # Iterate
    for i in range(0,iterations):
        days_to_spawn_list_2 = [0,0,0,0,0,0,0,0,0]
        for i in range(0,8):
            days_to_spawn_list_2[i] = days_to_spawn_list[i + 1]
        days_to_spawn_list_2[8] = days_to_spawn_list_2[8] + days_to_spawn_list[0]
        days_to_spawn_list_2[6] = days_to_spawn_list_2[6] + days_to_spawn_list[0]
        days_to_spawn_list = days_to_spawn_list_2

    # Calculate number of fish
    return sum(days_to_spawn_list)


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_6_data.csv"
    fish_data = get_csv_data_single_row(filepath)
    output = iterate_fish_version_2(fish_data, iterations=256)
    print(f"Final output: {output}")
