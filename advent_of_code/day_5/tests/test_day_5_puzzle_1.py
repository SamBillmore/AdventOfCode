from advent_of_code.utils.get_data import get_data_from_txt
from advent_of_code.day_5.solutions.day_5_puzzle_1 import data_munging


def test_data_munging():
    # Given
    filepath = "./advent_of_code/data/day_5_data.txt"
    input_data = get_data_from_txt(filepath)

    # When
    actual = data_munging(input_data)

    # Then
    expected = [((599,531),(599,32)),((435,904),(435,489))]
    assert actual[:2] == expected
