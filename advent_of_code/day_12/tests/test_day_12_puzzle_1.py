from advent_of_code.day_12.solutions.day_12_puzzle_1 import data_munging, find_all_routes, EXISTING_ROUTES, count_valid_routes


def test_data_munging_simple():
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

    # When the function is called
    actual = data_munging(input_data)

    # Then the output is as expected
    expected = [
        ['start', 'A'],
        ['start', 'b'],
        ['A', 'c'],
        ['c', 'A'],
        ['A', 'b'],
        ['b', 'A'],
        ['b', 'd'],
        ['d', 'b'],
        ['A', 'end'],
        ['b', 'end']
    ]
    assert actual == expected


def test_data_munging_complex():
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

    # When the function is called
    actual = data_munging(input_data)

    # Then the output is as expected
    expected = [
        ['dc', 'end'],
        ['start', 'HN'],
        ['start', 'kj'],
        ['start', 'dc'],
        ['dc', 'HN'],
        ['HN', 'dc'],
        ['LN', 'dc'],
        ['dc', 'LN'],
        ['HN', 'end'],
        ['kj', 'sa'],
        ['sa', 'kj'],
        ['kj', 'HN'],
        ['HN', 'kj'],
        ['kj', 'dc'],
        ['dc', 'kj']
    ]
    assert actual == expected


def test_find_all_routes_1():
    # Given some input data
    input_data = [
        ['start', 'b'],
        ['b', 'end']
    ]
    current_route = ['start']

    # When the function is called
    find_all_routes(input_data, current_route)
    actual = EXISTING_ROUTES

    # Then the output is as expected
    expected = [['start', 'b', 'end']]
    assert actual.sort() == expected.sort()


def test_find_all_routes_2():
    # Given some input data
    input_data = [
        ['start', 'b'],
        ['b', 'end'],
        ['start', 'bc'],
        ['bc', 'end']
    ]
    current_route = ['start']

    # When the function is called
    find_all_routes(input_data, current_route)
    actual = EXISTING_ROUTES

    # Then the output is as expected
    expected = [['start', 'b', 'end'], ['start', 'bc', 'end']]
    assert actual.sort() == expected.sort()


def test_find_all_routes_3():
    # Given some input data
    input_data = [
        ['start', 'b'],
        ['b', 'end'],
        ['start', 'bc'],
        ['bc', 'end'],
        ['b', 'bc'],
        ['bc', 'b']
    ]
    current_route = ['start']

    # When the function is called
    find_all_routes(input_data, current_route)
    actual = EXISTING_ROUTES

    # Then the output is as expected
    expected = [
        ['start', 'b', 'end'],
        ['start', 'b', 'bc', 'end'],
        ['start', 'b', 'bc', 'b', 'end'],
        ['start', 'bc', 'end'],
        ['start', 'bc', 'b', 'end'],
        ['start', 'bc', 'b', 'bc', 'end']
    ]
    assert actual.sort() == expected.sort()


def test_count_valid_routes_1():
    # Given some input data
    input_data = [
        ['start', 'b'],
        ['b', 'end'],
        ['start', 'bc'],
        ['bc', 'end'],
        ['b', 'bc'],
        ['bc', 'b']
    ]

    # When the function is called
    actual = count_valid_routes(input_data)

    # Then the output is as expected
    expected = 4
    assert actual == expected


def test_find_filtered_routes_2():
    # Given some input data
    input_data = [
        ['dc', 'end'],
        ['start', 'HN'],
        ['start', 'kj'],
        ['start', 'dc'],
        ['dc', 'HN'],
        ['HN', 'dc'],
        ['LN', 'dc'],
        ['dc', 'LN'],
        ['HN', 'end'],
        ['kj', 'sa'],
        ['sa', 'kj'],
        ['kj', 'HN'],
        ['HN', 'kj'],
        ['kj', 'dc'],
        ['dc', 'kj']
    ]

    # When the function is called
    actual = count_valid_routes(input_data)

    # Then the output is as expected
    expected = 19
    assert actual == expected
