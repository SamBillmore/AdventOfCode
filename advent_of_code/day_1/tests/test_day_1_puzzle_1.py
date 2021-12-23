import pandas as pd

from advent_of_code.day_1.solutions.day_1_puzzle_1 import data_munging, count_depth_increase_from_previous_measurement


def test_data_munging():
    # Given some input data
    input_data = pd.DataFrame(
        [[171],
         [173],
         [174],
         [163]]
    )

    # When we run the function
    actual = data_munging(input_data)

    # Then the result is as expected
    expected = [171,173,174,163]
    assert actual == expected


def test_count_depth_increase_from_previous_measurement():
    # Given some input data
    test_data = [1, 2, 5, 4, 6]

    # When we run the function
    actual = count_depth_increase_from_previous_measurement(test_data)

    # Then the result is as expected
    expected = 3
    assert actual == expected
