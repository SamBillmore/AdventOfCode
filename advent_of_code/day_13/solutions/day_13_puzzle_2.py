from typing import List, Tuple

from advent_of_code.utils.get_data import get_data_from_txt
from advent_of_code.day_13.solutions.day_13_puzzle_1 import data_munging, single_fold


def multiple_folds(dot_data: List[Tuple[int]], folds: List[Tuple[str, int]]) -> List[Tuple[int]]:
    for fold in folds:
        updated_dots = single_fold(dot_data, fold)
        dot_data = updated_dots
    return dot_data


def plot_dots(dot_data: List[Tuple[int]]):
    print('\n')
    max_x = max([dot[0] for dot in dot_data])
    max_y = max([dot[1] for dot in dot_data])
    output_plot = [[' ' for _ in range(0,max_x + 1)] for _ in range(0,max_y + 1)]
    for dot in dot_data:
        output_plot[dot[1]][dot[0]] = '#'
    for row in output_plot:
        print(''.join(row))
    return output_plot


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_13_data.txt"
    input_data = get_data_from_txt(filepath)
    munged_fold_data, munged_dot_data = data_munging(input_data)
    output_dot_data = multiple_folds(munged_dot_data, munged_fold_data)
    output = plot_dots(output_dot_data)
