from typing import Dict, List, Tuple
from tqdm import tqdm

from advent_of_code.utils.get_data import get_data_from_txt


def data_munging(input_data: List) -> Tuple[str, Dict[str, str]]:
    pair_insertions = {}
    for row in input_data:
        if '->' in row:
            split_row = row.split(' -> ')
            pair_insertions[split_row[0]] = split_row[1]
        else:
            starting_string = row
    return starting_string, pair_insertions


def insert_into_pairs(starting_string: str, pair_insertions: Dict[str, str], count_dict: Dict) -> Tuple[str,Dict[str, int]]:
    output_str = ''
    for i in range(1,len(starting_string)):
        current_pair = starting_string[i-1 : i + 1]
        first_letter = current_pair[0]
        second_letter = current_pair[1]
        new_letter = pair_insertions[current_pair]
        output_str = output_str + first_letter + new_letter
        if new_letter in count_dict:
            count_dict[new_letter] = count_dict[new_letter] + 1
        else:
            count_dict[new_letter] = 1
    return output_str + second_letter, count_dict


def iterate_insert_into_pairs(number_of_iters: int, starting_string: str, pair_insertions: Dict[str, str]) -> str:
    count_dict = {}
    for letter in starting_string:
        if letter in count_dict:
            count_dict[letter] = count_dict[letter] + 1
        else:
            count_dict[letter] = 1
    for _ in tqdm(range(0, number_of_iters)):
        starting_string, count_dict = insert_into_pairs(starting_string, pair_insertions, count_dict)
    return starting_string, count_dict


def find_most_and_least_common_delta(count_dict: Dict[str, int]):
    max_value = max(count_dict.values())
    min_value = min(count_dict.values())
    return int(max_value - min_value)


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_14_data.txt"
    input_data = get_data_from_txt(filepath)
    starting_string, pair_insertions = data_munging(input_data)
    output_string, count_dict = iterate_insert_into_pairs(10, starting_string, pair_insertions)
    output = find_most_and_least_common_delta(count_dict)
    print(f"Final output: {output}")
