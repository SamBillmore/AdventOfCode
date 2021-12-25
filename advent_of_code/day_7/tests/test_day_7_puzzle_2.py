from advent_of_code.day_7.solutions.day_7_puzzle_2 import calculate_fuel_2, find_position


def test_calculate_fuel_2():
    # Given some input data
    input_data = [16,1,2,0,4,2,7,1,2,14]
    horizontal_position = 5

    # When we call the function
    actual = calculate_fuel_2(input_data, horizontal_position)

    # Then the output is as expected
    expected = 168
    assert actual == expected


def test_find_position():
    # Given some input data
    input_data = [16,1,2,0,4,2,7,1,2,14]

    # When we call the function
    actual = find_position(input_data)

    # Then the output is as expected
    expected = 5
    assert actual == expected
