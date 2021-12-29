from typing import List, Tuple

from advent_of_code.utils.get_data import get_data_from_txt


def data_munging(input_data: List) -> Tuple[List[Tuple[str, int]], List[Tuple[int]]]:
    fold_instruction = 'fold along '
    fold_list = []
    dots_list = []
    for row in input_data:
        if row[:len(fold_instruction)] == fold_instruction:
            fold_instr = row[len(fold_instruction):].split('=')
            fold_instr = (fold_instr[0], int(fold_instr[1]))
            fold_list.append(fold_instr)
        else:
            dot_pos = tuple([int(x) for x in row.split(',')])
            dots_list.append(dot_pos)
    return fold_list, dots_list


def single_fold(dot_data: List[Tuple[int]], fold: Tuple[str, int]) -> List[Tuple[int]]:
    output_dot_data = []
    fold_location = fold[1]
    if fold[0] == 'x':
        for dot in dot_data:
            if dot[0] < fold_location:
                output_dot_data.append(dot)
            else:
                new_dot = (dot[0] - 2 * (dot[0] - fold_location), dot[1])
                output_dot_data.append(new_dot)
    else:
        for dot in dot_data:
            if dot[1] < fold_location:
                output_dot_data.append(dot)
            else:
                new_dot = (dot[0], dot[1] - 2 * (dot[1] - fold_location))
                output_dot_data.append(new_dot)
    return list(set(output_dot_data))


def num_dots_after_single_fold(output_dot_data: List[Tuple[int]]) -> int:
    return len(output_dot_data)


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_13_data.txt"
    input_data = get_data_from_txt(filepath)
    munged_fold_data, munged_dot_data = data_munging(input_data)
    output_dot_data = single_fold(munged_dot_data, munged_fold_data[0])
    output = num_dots_after_single_fold(output_dot_data)
    print(f"Final output: {output}")
