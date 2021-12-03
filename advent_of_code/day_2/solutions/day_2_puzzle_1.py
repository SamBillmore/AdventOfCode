from typing import List
from advent_of_code.utils.get_data import get_csv_data


def final_position(data_list : List) -> int:
    """ 
    """
    horizontal_position = 0
    depth = 0
    for combined_command in data_list:
        split_command = combined_command.split()
        if split_command[0] == 'forward':
            horizontal_position = horizontal_position + int(split_command[1])
        elif split_command[0] == 'down':
            depth = depth + int(split_command[1])
        elif split_command[0] == 'up':
            depth = depth - int(split_command[1])
    return horizontal_position * depth


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_2_data.csv"
    list_of_measurements = get_csv_data(filepath)
    depth_by_horiz = final_position(list_of_measurements)
    print(f"Final output: {depth_by_horiz}")
