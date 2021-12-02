from advent_of_code.day_2.solutions.day_2_puzzle_1 import final_position


def test_final_position():
    # Given some input data
    test_data = ['forward 5','down 7','forward 8','forward 1','forward 1','down 1','down 9','up 4']

    # When the function is run
    actual = final_position(test_data)

    # Then the output is as expected
    expected_depth = 5 + 8 + 1 + 1
    expected_horizontal = 7 + 1 + 9 - 4
    expected = expected_depth * expected_horizontal
    assert actual == expected
