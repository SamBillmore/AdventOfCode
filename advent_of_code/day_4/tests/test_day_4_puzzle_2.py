from advent_of_code.day_4.solutions.day_4_puzzle_2 import mark_and_check_all_boards_2

def test_mark_and_check_all_boards():
    # Given some input data
    drawn_numbers = [57, 58, 92, 62, 63, 55, 56, 14, 15, 24, 22]
    boards = [[[57, 80, 91, 40, 12], [62, 36, 72, 0, 20], [55, 60, 25, 92, 96], [14, 2, 17, 18, 86], [-1, 4, 90, 66, 38]],
              [[-1, -1, -1, -1, 24], [33, 40, 86, 28, 96], [4, 97, 90, 32, 13], [50, 38, 35, 14, 56], [73, 42, 9, 36, 67]]]

    # When we run the code
    actual = mark_and_check_all_boards_2(drawn_numbers, boards)

    # Then the result is as expected
    expected = (33 + 40 + 86 + 28 + 96 + 4 + 97 + 90 + 32 + 13 + 50 + 38 + 35 + 73 + 42 + 9 + 36 + 67) * 24
    assert actual == expected
