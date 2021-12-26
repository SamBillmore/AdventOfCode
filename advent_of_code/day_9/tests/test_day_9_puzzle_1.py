from advent_of_code.day_9.solutions.day_9_puzzle_1 import data_munging, find_low_points, calculate_risk_level_sum


def test_data_munging():
    # Given some input data
    input_data = [
        '2199943210',
        '3987894921',
        '9856789892',
        '8767896789',
        '9899965678'
    ]

    # When the function is called
    actual = data_munging(input_data)

    # Then the output is as expected
    expected = [
        [2,1,9,9,9,4,3,2,1,0],
        [3,9,8,7,8,9,4,9,2,1],
        [9,8,5,6,7,8,9,8,9,2],
        [8,7,6,7,8,9,6,7,8,9],
        [9,8,9,9,9,6,5,6,7,8]
    ]
    assert actual == expected


def test_find_low_points():
    # Given some input data
    height_map = [
        [2,1,9,9,9,4,3,2,1,0],
        [3,9,8,7,8,9,4,9,2,1],
        [9,8,5,6,7,8,9,8,9,2],
        [8,7,6,7,8,9,6,7,8,9],
        [9,8,9,9,9,6,5,6,7,8]
    ]

    # When the function is called
    actual = find_low_points(height_map)

    # Then the output is as expected
    expected = [1,0,5,5]
    assert actual == expected


def test_calculate_risk_level_sum():
    # Given some input data
    low_points = [1,0,5,5]

    # When the function is called
    actual = calculate_risk_level_sum(low_points)

    # Then the output is as expected
    expected = 15
    assert actual == expected
