import pandas as pd

from advent_of_code.day_3.solutions.day_3_puzzle_2 import create_df_from_binary, most_common_value, life_support, convert_row_to_integer
from advent_of_code.utils.get_data import get_data_from_txt


def test_get_data_from_txt():
    # Given some input data
    filepath = "./advent_of_code/data/day_3_data.txt"

    # When we run the function
    actual = get_data_from_txt(filepath)

    # Then the output is as expected
    expected = ['000110010001','101000110000','000110010111']
    assert actual[:3] == expected


def test_create_df_from_binary():
    # Given some input data
    input_data = ['000110010001','101000110000','000110010111']

    # When we run the function
    actual = create_df_from_binary(input_data)

    # Then the output is as expected
    expected = pd.DataFrame({
        0:[0,1,0],
        1:[0,0,0],
        2:[0,1,0],
        3:[1,0,1],
        4:[1,0,1],
        5:[0,0,0],
        6:[0,1,0],
        7:[1,1,1],
        8:[0,0,0],
        9:[0,0,1],
        10:[0,0,1],
        11:[1,0,1]
    })
    pd.testing.assert_frame_equal(actual, expected)

def test_most_common_value():
    # Given some input data
    input_data = pd.DataFrame({
        0:[0,1,0],
        1:[0,0,0],
        2:[0,1,0],
        3:[1,0,1],
        4:[1,0,1],
        5:[0,0,0],
        6:[0,1,0],
        7:[1,1,1],
        8:[0,0,0],
        9:[0,0,1],
        10:[0,0,1],
        11:[1,0,1]
    })
    column_header = 0
    calculation = 'oxygen'

    # When we run the function
    actual = most_common_value(input_data, column_header, calculation)

    # Then the output is as expected
    expected = pd.DataFrame({
        0:[0,0],
        1:[0,0],
        2:[0,0],
        3:[1,1],
        4:[1,1],
        5:[0,0],
        6:[0,0],
        7:[1,1],
        8:[0,0],
        9:[0,1],
        10:[0,1],
        11:[1,1]
    })
    pd.testing.assert_frame_equal(actual.reset_index(drop=True), expected)


def test_convert_row_to_integer():
    # Given some input data
    input_data = pd.DataFrame({
        0:[0],
        1:[0],
        2:[0],
        3:[1],
        4:[1],
        5:[0],
        6:[0],
        7:[1],
        8:[0],
        9:[1],
        10:[1],
        11:[1]
    })

    # When we run the function
    actual = convert_row_to_integer(input_data)

    # Then the output is as expected
    expected = 407
    assert actual == expected


def test_life_support():
    # Given some input data
    input_data = ['000110010001','101000110000','000110010111']

    # When we run the function
    actual = life_support(input_data)

    # Then the output is as expected
    expected = int('101000110000',2) * int('000110010111',2)
    assert actual == expected    
