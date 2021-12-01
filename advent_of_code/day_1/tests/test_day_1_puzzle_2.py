from advent_of_code.day_1.solutions.day_1_puzzle_2 import three_measurement_windows


def test_three_measurement_windows():
    # Given some input data
    test_data = [1, 2, 5, 4, 6, 0, 0, 0, 5]
    #                  8  11 15 10 6  0  5

    # When we run the function
    actual = three_measurement_windows(test_data)

    # Then the result is as expected
    expected = 3
    assert actual == expected
