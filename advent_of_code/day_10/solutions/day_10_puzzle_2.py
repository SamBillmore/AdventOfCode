from typing import List, Optional
from tqdm import tqdm
from statistics import median

from advent_of_code.utils.get_data import get_data_from_txt


def check_incomplete(input_data: List[str]) -> List:
    incomplete_rows = []
    for row in tqdm(input_data):
        incomplete_row = check_incomplete_single_row(row)
        if incomplete_row is not None:
            incomplete_rows.append(reverse_incomplete_row(incomplete_row))
    return incomplete_rows


def reverse_incomplete_row(incomplete_row: str) -> str:
    output = ''
    character_pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    reversed_row = incomplete_row[::-1]
    for character in reversed_row:
        output = output + character_pairs[character]
    return output


def check_incomplete_single_row(row: str) -> Optional[str]:
    closing_characters = [')',']','}','>']
    character_pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    row_length = len(row)
    position_index = 0
    for _ in range(0, row_length):
        if row[position_index] in closing_characters:
            if row[position_index - 1] != character_pairs[row[position_index]]:
                return None
            else:
                row = row.replace(character_pairs[row[position_index]] + row[position_index], '', 1)
                position_index = position_index - 1 
        else:
            position_index = position_index + 1
    return row


def calculate_autocomplete_score(closing_characters: List[str]) -> int:
    scores_dict = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    row_scores_list = []
    for row in closing_characters:
        row_score = 0
        for character in row:
            row_score = row_score * 5 + scores_dict[character]
        row_scores_list.append(row_score)
    return median(row_scores_list)


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_10_data.txt"
    input_data = get_data_from_txt(filepath)
    corrupted_characters = check_incomplete(input_data)
    output = calculate_autocomplete_score(corrupted_characters)
    print(f"Final output: {output}")
