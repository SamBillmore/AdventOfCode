from typing import List
from advent_of_code.utils.get_data import get_data_from_txt


def data_munging(input_data: List) -> List:
    output_data = []
    for row in input_data:
        row = [int(x) for x in row]
        output_data.append(row)
    return output_data


def find_low_points(height_map: List[List[int]]) -> List[int]:
    low_points = []
    max_row = len(height_map) - 1
    for count_row, row in enumerate(height_map):
        max_col = len(row) - 1
        for count_col, current_value in enumerate(row):
            top_point = 10
            bottom_point = 10
            left_point = 10
            right_point = 10
            if count_row > 0:
                top_point = height_map[count_row - 1][count_col]
            if count_row < max_row:
                bottom_point = height_map[count_row + 1][count_col]
            if count_col > 0:
                left_point = height_map[count_row][count_col - 1]
            if count_col < max_col:
                right_point = height_map[count_row][count_col + 1]
            if current_value < min([top_point, bottom_point, left_point, right_point]):
                low_points.append(current_value)
    return low_points


def calculate_risk_level_sum(low_points: List[int]) -> int:
    return sum([x + 1 for x in low_points])


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_9_data.txt"
    input_data = get_data_from_txt(filepath)
    height_map = data_munging(input_data)
    low_points = find_low_points(height_map)
    output = calculate_risk_level_sum(low_points)
    print(f"Final output: {output}")
