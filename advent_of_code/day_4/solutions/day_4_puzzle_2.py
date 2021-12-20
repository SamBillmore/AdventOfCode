from typing import List
import numpy as np

from advent_of_code.utils.get_data import get_data_from_txt
from advent_of_code.day_4.solutions.day_4_puzzle_1 import data_munging, mark_boards, check_boards, sum_board


def check_boards_2(boards: List[List[List[int]]]) -> bool:
    completed_boards = []
    for board in boards:
        np_board = np.array(board)
        column_sum = np.sum(np_board, axis=0)
        row_sum = np.sum(np_board, axis=1)
        if -5 in column_sum or -5 in row_sum:
            completed_boards.append(board)
    return completed_boards


def mark_and_check_all_boards_2(drawn_numbers: List[int], boards: List[List[List[int]]]) -> int:
    for drawn_number in drawn_numbers:
        print(drawn_number)
        boards = mark_boards(drawn_number, boards)
        completed_boards = check_boards_2(boards)
        if len(completed_boards) > 0:
            if len(boards) > 1:
                for board in completed_boards:
                    boards.remove(board)
            else:
                return drawn_number * sum_board(boards[0])
        print('Length boards: ', len(boards))


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_4_data.txt"
    input_data = get_data_from_txt(filepath)
    drawn_numbers, boards = data_munging(input_data)
    output = mark_and_check_all_boards_2(drawn_numbers, boards)
    print(f"Final output: {output}")
