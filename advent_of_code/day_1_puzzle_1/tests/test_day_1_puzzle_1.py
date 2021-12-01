from advent_of_code.day_1_puzzle_1.solution.day_1_puzzle_1 import count_depth_increase_from_previous_measurement


def test_count_depth_increase_from_previous_measurement():
    # Given some input data
    test_data = [1, 2, 5, 4, 6]

    # When we run the function
    actual = count_depth_increase_from_previous_measurement(test_data)

    # Then the result is as expected
    expected = 3
    assert actual == expected
