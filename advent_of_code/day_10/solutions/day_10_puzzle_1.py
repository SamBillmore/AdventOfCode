from typing import List, Optional
from tqdm import tqdm

from advent_of_code.utils.get_data import get_data_from_txt


def check_corrupted(input_data: List[str]) -> List:
    corrupted_rows = []
    for row in tqdm(input_data):
        corrupted_row = check_corrupted_single_row(row)
        if corrupted_row is not None:
            corrupted_rows.append(corrupted_row)
    return corrupted_rows


def check_corrupted_single_row(row: str) -> Optional[str]:
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
                return row[position_index]
            else:
                row = row.replace(character_pairs[row[position_index]] + row[position_index], '', 1)
                position_index = position_index - 1 
        else:
            position_index = position_index + 1
    return None


def calculate_score(corrupted_characters: List[str]) -> int:
    score_lookup_dict = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    score = 0
    for character in corrupted_characters:
        score = score + score_lookup_dict[character]
    return score


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_10_data.txt"
    input_data = get_data_from_txt(filepath)
    corrupted_characters = check_corrupted(input_data)
    output = calculate_score(corrupted_characters)
    print(f"Final output: {output}")
