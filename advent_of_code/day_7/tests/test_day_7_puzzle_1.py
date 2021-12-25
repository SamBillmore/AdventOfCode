from advent_of_code.day_7.solutions.day_7_puzzle_1 import find_horizontal_position, calculate_fuel


def test_find_horizontal_position():
    # Given some input data
    input_data = [16,1,2,0,4,2,7,1,2,14]

    # When we run the function
    actual = find_horizontal_position(input_data)

    # Then the result is as expected
    expected = 2
    assert actual == expected


def test_calculate_fuel():
    # Given some input data
    input_data = [16,1,2,0,4,2,7,1,2,14]
    horizontal_position = 2

    # When we run the function
    actual = calculate_fuel(input_data, horizontal_position)

    # The the result is as expected
    expected = 37
    assert actual == expected
