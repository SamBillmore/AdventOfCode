from typing import List, Tuple
import numpy as np

from advent_of_code.utils.get_data import get_data_from_txt


def data_munging(input_data: List) -> Tuple[List[int], List[List[List[int]]]]:
    drawn_list = input_data[0].split(',')
    drawn_list = [int(x) for x in drawn_list]

    board = []
    boards = []
    for count, entry in enumerate(input_data[1:]):
        row = entry.replace('  ', ' ').strip().split()
        row = [int(x) for x in row]
        board.append(row)
        if (count + 1) % 5 == 0:
            boards.append(board)
            board = []
    return drawn_list, boards


def mark_boards(drawn_number: int, boards: List[List[List[int]]]) -> List[List[List[int]]]:
    return [[[-1 if x == drawn_number else x for x in row] for row in board] for board in boards]


def check_boards(boards: List[List[List[int]]]) -> bool:
    for board in boards:
        np_board = np.array(board)
        column_sum = np.sum(np_board, axis=0)
        row_sum = np.sum(np_board, axis=1)
        if -5 in column_sum or -5 in row_sum:
            return board
    return False


def sum_board(board: List[List[int]]) -> int:
    board = [[0 if x == -1 else x for x in row] for row in board]
    return sum([sum(row) for row in board])


def mark_and_check_all_boards(drawn_numbers: List[int], boards: List[List[List[int]]]) -> int:
    for drawn_number in drawn_numbers:
        boards = mark_boards(drawn_number, boards)
        board = check_boards(boards)
        if board:
            return drawn_number * sum_board(board)


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_4_data.txt"
    input_data = get_data_from_txt(filepath)
    drawn_numbers, boards = data_munging(input_data)
    output = mark_and_check_all_boards(drawn_numbers, boards)
    print(f"Final output: {output}")
