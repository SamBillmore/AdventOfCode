from advent_of_code.day_6.solutions.day_6_puzzle_1 import data_munging, single_fish_iteration, iterate_fish, count_fish


def test_data_munging():
    # Given some input data
    input_data = ['1,2,3,4,5']

    # When we run the funtion
    actual = data_munging(input_data)

    # Then the output is as expected
    expected = [1,2,3,4,5]
    assert actual == expected


def test_single_fish_iteration():
    # Given some input data
    munged_data = [0,1,2,3,4,5]

    # When we run the funtion
    actual = single_fish_iteration(munged_data)

    # Then the output is as expected
    expected = [6,0,1,2,3,4,8]
    assert actual == expected


def test_iterate_fish():
    # Given some input data
    fish_data = [0,1,2,3,4,5]
    iterations = 3
    # [6,0,1,2,3,4,8]
    # [5,6,0,1,2,3,7,8]
    # [4,5,6,0,1,2,6,7,8]

    # When we run the funtion
    actual = iterate_fish(fish_data, iterations)

    # Then the output is as expected
    expected = [4,5,6,0,1,2,6,7,8]
    assert actual == expected


def test_count_fish():
    # Given some input data
    fish_data = [0,1,2,3,4,5]

    # When we run the funtion
    actual = count_fish(fish_data)

    # Then the output is as expected
    expected = 6
    assert actual == expected
