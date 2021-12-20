from advent_of_code.day_4.solutions.day_4_puzzle_1 import data_munging, mark_boards, check_boards, mark_and_check_all_boards, sum_board
from advent_of_code.utils.get_data import get_data_from_txt


def test_data_munging():
    # Given some input data
    filepath = "./advent_of_code/data/day_4_data.txt"
    input_data = get_data_from_txt(filepath)

    # When we run the code
    actual_drawn, actual_boards = data_munging(input_data)
    actual_first_board = actual_boards[0]

    # Then the result is as expected
    expected_drawn = [17,11,37,7,89,48,99,28,56,55,57,27,83,59,53,72,6,87,33,82,13,23,35,40,71,47,78,2,39,4,51,1,67,31,79,69,15,73,80,22,92,95,91,43,26,97,36,34,12,96,86,52,66,94,61,76,64,77,85,98,42,68,84,63,60,30,65,19,54,58,24,20,25,75,93,16,18,44,14,88,45,10,9,3,70,74,81,90,46,38,21,49,29,50,0,5,8,32,62,41]
    expected_first_board = [[57,80,91,40,12],
                            [62,36,72,0,20],
                            [55,60,25,92,96],
                            [14,2,17,18,86],
                            [1,4,90,66,38]]
    assert actual_drawn == expected_drawn
    assert actual_first_board == expected_first_board


def test_mark_boards():
    # Given some input data
    drawn_number = 1
    boards = [[[57, 80, 91, 40, 12], [62, 36, 72, 0, 20], [55, 60, 25, 92, 96], [14, 2, 17, 18, 86], [1, 4, 90, 66, 38]],
              [[1, 25, 81, 16, 24], [33, 40, 86, 28, 96], [4, 97, 90, 32, 13], [50, 38, 35, 14, 56], [73, 42, 9, 36, 67]]]

    # When we run the code
    actual = mark_boards(drawn_number, boards)

    # Then the result is as expected
    expected = [[[57, 80, 91, 40, 12], [62, 36, 72, 0, 20], [55, 60, 25, 92, 96], [14, 2, 17, 18, 86], [-1, 4, 90, 66, 38]],
                [[-1, 25, 81, 16, 24], [33, 40, 86, 28, 96], [4, 97, 90, 32, 13], [50, 38, 35, 14, 56], [73, 42, 9, 36, 67]]]
    assert actual == expected


def test_check_boards_no_match():
    # Given some input data
    boards = [[[57, 80, 91, 40, 12], [62, 36, 72, 0, 20], [55, 60, 25, 92, 96], [14, 2, 17, 18, 86], [-1, 4, 90, 66, 38]],
              [[-1, 25, 81, 16, 24], [33, 40, 86, 28, 96], [4, 97, 90, 32, 13], [50, 38, 35, 14, 56], [73, 42, 9, 36, 67]]]

    # When we run the code
    actual = check_boards(boards)

    # Then the result is as expected
    expected = False
    assert actual == expected


def test_check_boards_row_match():
    # Given some input data
    boards = [[[57, 80, 91, 40, 12], [62, 36, 72, 0, 20], [55, 60, 25, 92, 96], [14, 2, 17, 18, 86], [-1, 4, 90, 66, 38]],
              [[-1, -1, -1, -1, -1], [33, 40, 86, 28, 96], [4, 97, 90, 32, 13], [50, 38, 35, 14, 56], [73, 42, 9, 36, 67]]]

    # When we run the code
    actual = check_boards(boards)

    # Then the result is as expected
    expected = [[-1, -1, -1, -1, -1], [33, 40, 86, 28, 96], [4, 97, 90, 32, 13], [50, 38, 35, 14, 56], [73, 42, 9, 36, 67]]
    assert actual == expected


def test_check_boards_column_match():
    # Given some input data
    boards = [[[57, 80, 91, 40, 12], [62, 36, 72, 0, 20], [55, 60, 25, 92, 96], [14, 2, 17, 18, 86], [-1, 4, 90, 66, 38]],
              [[-1, 25, 81, 16, 24], [-1, 40, 86, 28, 96], [-1, 97, 90, 32, 13], [-1, 38, 35, 14, 56], [-1, 42, 9, 36, 67]]]

    # When we run the code
    actual = check_boards(boards)

    # Then the result is as expected
    expected = [[-1, 25, 81, 16, 24], [-1, 40, 86, 28, 96], [-1, 97, 90, 32, 13], [-1, 38, 35, 14, 56], [-1, 42, 9, 36, 67]]
    assert actual == expected


def test_sum_board():
    # Given some input data
    board = [[57, 80, 91, 40, 12], [62, 36, 72, 0, 20], [55, 60, 25, 92, 96], [14, 2, 17, 18, 86], [-1, 4, 90, 66, 38]]

    # When we run the code
    actual = sum_board(board)

    # Then the result is as expected
    expected = 57 + 80 + 91 + 40 + 12 + 62 + 36 + 72 + 0 + 20 + 55 + 60 + 25 + 92 + 96 + 14 + 2 + 17 + 18 + 86 + 0 + 4 + 90 + 66 + 38
    assert actual == expected


def test_mark_and_check_all_boards():
    # Given some input data
    drawn_numbers = [57,58,92,62,63,55,56,14,15]
    boards = [[[57, 80, 91, 40, 12], [62, 36, 72, 0, 20], [55, 60, 25, 92, 96], [14, 2, 17, 18, 86], [-1, 4, 90, 66, 38]],
              [[-1, 25, 81, 16, 24], [33, 40, 86, 28, 96], [4, 97, 90, 32, 13], [50, 38, 35, 14, 56], [73, 42, 9, 36, 67]]]

    # When we run the code
    actual = mark_and_check_all_boards(drawn_numbers, boards)

    # Then the result is as expected
    expected = (80 + 91 + 40 + 12 + 36 + 72 + 0 + 20 + 60 + 25 + 96 + 2 + 17 + 18 + 86 + 4 + 90 + 66 + 38) * 14
    assert actual == expected
