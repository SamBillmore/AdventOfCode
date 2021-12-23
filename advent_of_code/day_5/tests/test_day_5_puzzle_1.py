from numpy import exp
import pandas as pd

from advent_of_code.day_5.solutions.day_5_puzzle_1 import data_munging, create_blank_diagram, update_diagram_horiz_vert, count_overlapping_lines


def test_data_munging():
    input_data = ['599,531 -> 599,32', '435,904 -> 435,489']

    # When we run the function
    actual = data_munging(input_data)

    # Then the result is as expected
    expected = [((599,531),(599,32)),((435,904),(435,489))]
    assert actual == expected


def test_create_blank_diagram():
    # Given input data
    input_data = [((10,7),(3,3)),((9,9),(1,1))]

    # When the function is called
    actual = create_blank_diagram(input_data)

    # Then the output is as expected
    expected = pd.DataFrame({
        0:[0,0,0,0,0,0,0,0,0,0,0],
        1:[0,0,0,0,0,0,0,0,0,0,0],
        2:[0,0,0,0,0,0,0,0,0,0,0],
        3:[0,0,0,0,0,0,0,0,0,0,0],
        4:[0,0,0,0,0,0,0,0,0,0,0],
        5:[0,0,0,0,0,0,0,0,0,0,0],
        6:[0,0,0,0,0,0,0,0,0,0,0],
        7:[0,0,0,0,0,0,0,0,0,0,0],
        8:[0,0,0,0,0,0,0,0,0,0,0],
        9:[0,0,0,0,0,0,0,0,0,0,0]
    })
    pd.testing.assert_frame_equal(actual, expected)


def test_update_diagram_horiz_vert():
    # Given some input data
    test_munged_data = [((0,2),(0,3)),
                        ((1,1),(4,4)),
                        ((0,2),(1,2))]
    test_blank_diagram = pd.DataFrame(
        [[0] * (4 + 1)] * (4 + 1)
    )

    # When we run the function
    actual = update_diagram_horiz_vert(test_munged_data, test_blank_diagram)

    # Then the output is as expected
    expected = pd.DataFrame(
        [[0,0,0,0,0],
         [0,0,0,0,0],
         [2,1,0,0,0],
         [1,0,0,0,0],
         [0,0,0,0,0]]
    )
    pd.testing.assert_frame_equal(actual, expected)


def test_count_overlapping_lines():
    # Given some input data
    input_diagram = pd.DataFrame(
        [[0,0,0,1,0],
         [0,0,1,2,1],
         [2,1,0,1,0],
         [1,0,0,1,0],
         [0,1,2,3,1]]
    )

    # When we run the function
    actual = count_overlapping_lines(input_diagram)

    # Then the output is as expected
    expected = 4
    assert actual == expected
