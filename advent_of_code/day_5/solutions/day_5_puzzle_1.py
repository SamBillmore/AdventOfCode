import pandas as pd
import numpy as np
from typing import List, Tuple
from advent_of_code.utils.get_data import get_data_from_txt


def data_munging(input_data: List) -> List[Tuple[Tuple]]:
    """
    """
    output_list = []
    for entry in input_data:
        row_list = []
        row = entry.split(' -> ')
        for pair in row:
            pair_list = []
            pair = pair.split(',')
            for item in pair:
                item = int(item)
                pair_list.append(item)
            row_list.append(tuple(pair_list))
        output_list.append(tuple(row_list))
    return output_list


def create_blank_diagram(munged_data: List[Tuple[Tuple]]) -> pd.DataFrame:
    """
    """
    max_x = 0
    max_y = 0
    for row in munged_data:
        for pair in row:
            x = pair[0]
            y = pair[1]
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
    data = [[0] * (max_y + 1)] * (max_x + 1)  # NB: +1 is to account for 0 indexing
    return pd.DataFrame(data)


def update_diagram_horiz_vert(munged_data: List[Tuple[Tuple]], current_diagram: pd.DataFrame) -> pd.DataFrame:
    """
    """
    for row in munged_data:
        pair_1 = row[0]
        pair_1_x = pair_1[0]
        pair_1_y = pair_1[1]
        pair_2 = row[1]
        pair_2_x = pair_2[0]
        pair_2_y = pair_2[1]
        if pair_1_x == pair_2_x:
            min_y = min(pair_1_y, pair_2_y)
            max_y = max(pair_1_y, pair_2_y)
            for y in range(min_y, max_y+1):
                current_diagram.at[y, pair_1_x] = current_diagram.at[y, pair_1_x] + 1
        if pair_1_y == pair_2_y:
            min_x = min(pair_1_x, pair_2_x)
            max_x = max(pair_1_x, pair_2_x)
            for x in range(min_x, max_x+1):
                current_diagram.at[pair_1_y, x] = current_diagram.at[pair_1_y, x] + 1
    return current_diagram


def count_overlapping_lines(diagram: pd.DataFrame) -> int:
    """
    """
    return sum(diagram[diagram > 1].count())


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_5_data.txt"
    input_data = get_data_from_txt(filepath)
    munged_data = data_munging(input_data)
    blank_diagram = create_blank_diagram(munged_data)
    current_diagram = update_diagram_horiz_vert(munged_data, blank_diagram)
    output = count_overlapping_lines(current_diagram)
    print(f"Final output: {output}")
