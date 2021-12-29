from advent_of_code.day_13.solutions.day_13_puzzle_1 import data_munging, single_fold


def test_data_munging():
    # Given some input data
    input_data = [
        '6,10',
        '0,14',
        '9,10',
        '0,3',
        '10,4',
        '4,11',
        '6,0',
        '6,12',
        '4,1',
        '0,13',
        '10,12',
        '3,4',
        '3,0',
        '8,4',
        '1,10',
        '2,14',
        '8,10',
        '9,0',
        'fold along y=7',
        'fold along x=5'
    ]

    # When the function is called
    actual_fold_list, actual_dots_list = data_munging(input_data)

    # Then the output is as expected
    expected_fold_list = [
        ('y', 7),
        ('x', 5)
    ]
    expected_dots_list = [
        (6,10),
        (0,14),
        (9,10),
        (0,3),
        (10,4),
        (4,11),
        (6,0),
        (6,12),
        (4,1),
        (0,13),
        (10,12),
        (3,4),
        (3,0),
        (8,4),
        (1,10),
        (2,14),
        (8,10),
        (9,0)
    ]
    assert actual_fold_list == expected_fold_list
    assert actual_dots_list == expected_dots_list


def test_single_fold():
    # Given some input data
    input_data = [
        (6,10),
        (0,14),
        (9,10),
        (0,3),
        (10,4),
        (4,11),
        (6,0),
        (6,12),
        (4,1),
        (0,13),
        (10,12),
        (3,4),
        (3,0),
        (8,4),
        (1,10),
        (2,14),
        (8,10),
        (9,0)
    ]
    fold = ('y', 7)

    # When the function is called
    actual = single_fold(input_data, fold)

    # Then the output is as expected
    expected = [
        (0,0),
        (2,0),
        (3,0),
        (6,0),
        (9,0),
        (0,1),
        (4,1),
        (6,2),
        (10,2),
        (0,3),
        (4,3),
        (1,4),
        (3,4),
        (6,4),
        (8,4),
        (9,4),
        (10,4)
    ]
    assert actual.sort() == expected.sort()
