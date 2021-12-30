from typing import Dict, Tuple
from tqdm import tqdm

from advent_of_code.utils.get_data import get_data_from_txt
from advent_of_code.day_14.solutions.day_14_puzzle_1 import data_munging, find_most_and_least_common_delta


def create_initial_pairs_dict(starting_string: str) -> Tuple[Dict[str, int], str]:
    pairs_dict = {}
    for i in range(1,len(starting_string)):
        current_pair = starting_string[i-1 : i + 1]
        if current_pair in pairs_dict:
            pairs_dict[current_pair] = pairs_dict[current_pair] + 1
        else:
            pairs_dict[current_pair] = 1
    return pairs_dict
        
        
def update_pairs_dict(pairs_dict: Dict[str, int], pair_insertions: Dict[str, str]) -> Dict[str, int]:
    new_pairs_dict = {}
    for pair in pairs_dict.keys():
        pair_value = pairs_dict[pair]
        first_letter = pair[0]
        second_letter = pair[1]
        new_letter = pair_insertions[pair]
        first_new_pair = first_letter + new_letter
        second_new_pair = new_letter + second_letter
        for new_pair in [first_new_pair, second_new_pair]:
            if new_pair in new_pairs_dict:
                new_pairs_dict[new_pair] = new_pairs_dict[new_pair] + pair_value
            else:
                new_pairs_dict[new_pair] = pair_value
    return new_pairs_dict


def iterate_update_pairs_dict(number_of_iters: int, initial_pairs_dict: Dict[str, int], pair_insertions: Dict[str, str]) -> Dict[str, int]:
    for _ in tqdm(range(0, number_of_iters)):
        initial_pairs_dict = update_pairs_dict(initial_pairs_dict, pair_insertions)
    return initial_pairs_dict


def convert_pair_dict_to_count_dict(pair_dict: Dict[str, int], starting_string: str) -> Dict[str, int]:
    count_dict = {}
    for pair, pair_count in pair_dict.items():
        for pair_letter in pair:
            if pair_letter in count_dict:
                    count_dict[pair_letter] = count_dict[pair_letter] + pair_count
            else:
                count_dict[pair_letter] = pair_count
    start_letter = starting_string[0]
    end_letter = starting_string[-1]
    count_dict[start_letter] = count_dict[start_letter] - 1
    count_dict[end_letter] = count_dict[end_letter] - 1
    for letter, letter_count in count_dict.items():
        count_dict[letter] = letter_count / 2
    count_dict[start_letter] = count_dict[start_letter] + 1
    count_dict[end_letter] = count_dict[end_letter] + 1
    return count_dict


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_14_data.txt"
    input_data = get_data_from_txt(filepath)
    starting_string, pair_insertions = data_munging(input_data)
    initial_pairs_dict = create_initial_pairs_dict(starting_string)
    final_pairs_dict = iterate_update_pairs_dict(40, initial_pairs_dict, pair_insertions)
    count_dict = convert_pair_dict_to_count_dict(final_pairs_dict, starting_string)
    output = find_most_and_least_common_delta(count_dict)
    print(f"Final output: {output}")
