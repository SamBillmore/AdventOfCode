import pandas as pd

from advent_of_code.day_5.solutions.day_5_puzzle_2 import update_diagram_diagonal


def test_update_diagram_diagonal():
    # Given input data
    test_munged_data = [((0,2),(0,3)),
                        ((1,1),(4,4)),
                        ((0,2),(1,2))]
    test_current_diagram = pd.DataFrame(
        [[0,0,0,0,0],
         [0,0,0,0,0],
         [2,1,0,0,0],
         [1,0,0,0,0],
         [0,0,0,0,0]]
    )

    # When we run the function
    actual = update_diagram_diagonal(test_munged_data, test_current_diagram)

    # Then the output is as expected
    expected = pd.DataFrame(
        [[0,0,0,0,0],
         [0,1,0,0,0],
         [2,1,1,0,0],
         [1,0,0,1,0],
         [0,0,0,0,1]]
    )
    pd.testing.assert_frame_equal(actual, expected)
