from advent_of_code.day_3.solutions.day_3_puzzle_1 import power_consumption

from advent_of_code.utils.get_data import get_binary_data


def test_power_consumption():
    # Given some input data
    test_data = [b'000110010001',
                 b'101000110000',
                 b'000110010111']
    # Most common  000110010001

    # When the function is run
    actual = power_consumption(test_data)

    # Then the output is as expected
    expected_gamma_byte = b'000110010001'
    expected_epsilon_byte = b'111001101110'
    expected_gamma = int(expected_gamma_byte, 2)
    expected_epsilon = int(expected_epsilon_byte, 2)
    expected = expected_gamma * expected_epsilon
    assert actual == expected


def test_get_binary_data():
    # Given some input data
    filepath = "./advent_of_code/data/day_3_data.bin"

    # When we run the function
    actual = get_binary_data(filepath)

    # Then the output is as expected
    expected = [b'000110010001', b'101000110000', b'000110010111']
    assert actual[:3] == expected
