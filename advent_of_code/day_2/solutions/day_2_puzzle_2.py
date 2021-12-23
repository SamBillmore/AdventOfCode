from typing import List
from advent_of_code.utils.get_data import get_csv_data
from advent_of_code.day_1.solutions.day_1_puzzle_1 import data_munging


def final_position_2(data_list : List) -> int:
    """ 
    """
    horizontal_position = 0
    depth = 0
    aim = 0
    for combined_command in data_list:
        split_command = combined_command.split()
        if split_command[0] == 'forward':
            horizontal_position = horizontal_position + int(split_command[1])
            depth = depth + aim * int(split_command[1])
        elif split_command[0] == 'down':
            aim = aim + int(split_command[1])
        elif split_command[0] == 'up':
            aim = aim - int(split_command[1])
    return horizontal_position * depth


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_2_data.csv"
    input_data = get_csv_data(filepath)
    list_of_measurements = data_munging(input_data)
    depth_by_horiz = final_position_2(list_of_measurements)
    print(f"Final output: {depth_by_horiz}")
