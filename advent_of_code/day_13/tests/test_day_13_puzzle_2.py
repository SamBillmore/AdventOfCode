from advent_of_code.day_13.solutions.day_13_puzzle_2 import multiple_folds, plot_dots


def test_multiple_folds():
    # Given some input data
    input_dot_list = [
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
    input_folds = [
        ('y', 7),
        ('x', 5)
    ]

    # When the function is called
    actual = multiple_folds(input_dot_list, input_folds)

    # Then the output is as expected
    expected = [
        (0,0),
        (1,0),
        (2,0),
        (3,0),
        (4,0),
        (0,4),
        (1,4),
        (2,4),
        (3,4),
        (4,4),
        (0,0),
        (0,1),
        (0,2),
        (0,3),
        (0,4),
        (4,0),
        (4,1),
        (4,2),
        (4,3),
        (4,4)
    ]
    assert actual.sort() == expected.sort()


def test_plot_dots():
    # Given some input data
    input_data = [
        (0,0),
        (1,0),
        (2,0),
        (3,0),
        (4,0),
        (0,4),
        (1,4),
        (2,4),
        (3,4),
        (4,4),
        (0,0),
        (0,1),
        (0,2),
        (0,3),
        (0,4),
        (4,0),
        (4,1),
        (4,2),
        (4,3),
        (4,4)
    ]

    # When the function is called
    actual = plot_dots(input_data)

    # Then the output is as expected
    expected = [
        ['#','#','#','#','#'],
        ['#','.','.','.','#'],
        ['#','.','.','.','#'],
        ['#','.','.','.','#'],
        ['#','#','#','#','#']
    ]
    assert actual == expected
