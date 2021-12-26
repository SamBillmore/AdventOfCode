from typing import List
from advent_of_code.utils.get_data import get_data_from_txt


def data_munging(input_data: List) -> List:
    """
    """
    output_data = []
    for row in input_data:
        row = row.split(' | ')
        new_row = []
        for segments_group in row:
            segments_group = segments_group.split()
            new_row.append(segments_group)
        output_data.append(new_row)
    return output_data


def count_1_4_7_8(segment_data):
    """
    """
    unique_digit_lengths = [2,3,4,7]
    count = 0
    for row in segment_data:
        four_digit_output = row[1]
        for segment in four_digit_output:
            if len(segment) in unique_digit_lengths:
                count += 1
    return count


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_8_data.txt"
    input_data = get_data_from_txt(filepath)
    segment_data = data_munging(input_data)
    output = count_1_4_7_8(segment_data)
    print(f"Final output: {output}")
