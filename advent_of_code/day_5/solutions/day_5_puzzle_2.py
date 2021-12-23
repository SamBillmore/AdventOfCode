import pandas as pd
from typing import List, Tuple

from advent_of_code.utils.get_data import get_data_from_txt
from advent_of_code.day_5.solutions.day_5_puzzle_1 import data_munging, create_blank_diagram, update_diagram_horiz_vert, count_overlapping_lines


def update_diagram_diagonal(munged_data: List[Tuple[Tuple]], current_diagram: pd.DataFrame) -> pd.DataFrame:
    """
    """
    for row in munged_data:
        pair_1 = row[0]
        pair_1_x = pair_1[0]
        pair_1_y = pair_1[1]
        pair_2 = row[1]
        pair_2_x = pair_2[0]
        pair_2_y = pair_2[1]
        if pair_1_x != pair_2_x and pair_1_y != pair_2_y:
            if pair_1_x < pair_2_x and pair_1_y < pair_2_y:
                for x in range(pair_1_x, pair_2_x + 1, 1):
                    y = pair_1_y + (x - pair_1_x)
                    current_diagram.at[y, x] = current_diagram.at[y, x] + 1
            if pair_1_x > pair_2_x and pair_1_y < pair_2_y:
                for x in range(pair_1_x, pair_2_x - 1, -1):
                    y = pair_1_y - (x - pair_1_x)
                    current_diagram.at[y, x] = current_diagram.at[y, x] + 1
            if pair_1_x < pair_2_x and pair_1_y > pair_2_y:
                for x in range(pair_1_x, pair_2_x + 1, 1):
                    y = pair_1_y - (x - pair_1_x)
                    current_diagram.at[y, x] = current_diagram.at[y, x] + 1
            if pair_1_x > pair_2_x and pair_1_y > pair_2_y:
                for x in range(pair_1_x, pair_2_x - 1, -1):
                    y = pair_1_y + (x - pair_1_x)
                    current_diagram.at[y, x] = current_diagram.at[y, x] + 1
    return current_diagram


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_5_data.txt"
    input_data = get_data_from_txt(filepath)
    munged_data = data_munging(input_data)
    blank_diagram = create_blank_diagram(munged_data)
    current_diagram = update_diagram_horiz_vert(munged_data, blank_diagram)
    current_diagram = update_diagram_diagonal(munged_data, current_diagram)
    output = count_overlapping_lines(current_diagram)
    print(f"Final output: {output}")