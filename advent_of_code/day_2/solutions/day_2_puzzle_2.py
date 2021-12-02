from typing import List
from advent_of_code.utils.get_data import get_data


def final_position_2(data_list : List) -> int:
    """ 
    """
    pass


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_2_data.csv"
    list_of_measurements = get_data(filepath)
    depth_by_horiz = final_position_2(list_of_measurements)
    print(f"Final output: {depth_by_horiz}")
