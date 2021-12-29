from advent_of_code.day_12.solutions.day_12_puzzle_1 import data_munging
from advent_of_code.day_12.solutions.day_12_puzzle_2 import count_valid_routes_2


def test_count_valid_routes_2_version_1():
    # Given some input data
    input_data = [
        'start-A',
        'start-b',
        'A-c',
        'A-b',
        'b-d',
        'A-end',
        'b-end'
    ]
    # [
    #     'dc-end',
    #     'HN-start',
    #     'start-kj',
    #     'dc-start',
    #     'dc-HN',
    #     'LN-dc',
    #     'HN-end',
    #     'kj-sa',
    #     'kj-HN',
    #     'kj-dc'
    # ]
    munged_data = data_munging(input_data)

    # When the function is called
    actual = count_valid_routes_2(munged_data)

    # Then the output is as expected
    expected = 36
    # expected = 103
    assert actual == expected


def test_count_valid_routes_2_version_2():
    # Given some input data
    input_data = [
        'dc-end',
        'HN-start',
        'start-kj',
        'dc-start',
        'dc-HN',
        'LN-dc',
        'HN-end',
        'kj-sa',
        'kj-HN',
        'kj-dc'
    ]
    munged_data = data_munging(input_data)

    # When the function is called
    actual = count_valid_routes_2(munged_data)

    # Then the output is as expected
    expected = 103
    assert actual == expected


def test_count_valid_routes_2_version_3():
    # Given some input data
    input_data = [
        'fs-end',
        'he-DX',
        'fs-he',
        'start-DX',
        'pj-DX',
        'end-zg',
        'zg-sl',
        'zg-pj',
        'pj-he',
        'RW-he',
        'fs-DX',
        'pj-RW',
        'zg-RW',
        'start-pj',
        'he-WI',
        'zg-he',
        'pj-fs',
        'start-RW'
    ]
    munged_data = data_munging(input_data)

    # When the function is called
    actual = count_valid_routes_2(munged_data)

    # Then the output is as expected
    expected = 3509
    assert actual == expected
