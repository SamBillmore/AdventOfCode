from advent_of_code.day_2.solutions.day_2_puzzle_2 import final_position_2

def test_final_position_2():
    # Given some input data
    test_data = ['forward 5','down 7','forward 8','forward 1','forward 1','down 1','down 9','up 4','forward 6']
    # Aim                 0        7           7           7           7        8        17     13          13
    # Horizontal          5                    8           1           1                                    6
    # Depth               0*5                  7*8         7*1         7*1                                  13*6

    # When the function is run
    actual = final_position_2(test_data)

    # Then the output is as expected
    expected_horizontal = 5 + 8 + 1 + 1 + 6
    expected_depth = 0*5 + 7*8 + 7*1 + 7*1 + 13*6
    expected = expected_depth * expected_horizontal
    assert actual == expected
