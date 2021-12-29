from advent_of_code.day_14.solutions.day_14_puzzle_1 import data_munging, insert_into_pairs, iterate_insert_into_pairs, find_most_and_least_common_delta


def test_data_munging():
    # Given some input data
    input_data = [
        'NNCB',
        'CH -> B',
        'HH -> N',
        'CB -> H',
        'NH -> C',
        'HB -> C',
        'HC -> B',
        'HN -> C',
        'NN -> C',
        'BH -> H',
        'NC -> B',
        'NB -> B',
        'BN -> B',
        'BB -> N',
        'BC -> B',
        'CC -> N',
        'CN -> C'
    ]

    # When the function is called
    actual_starting_string, actual_pair_insertions = data_munging(input_data)

    # Then the output is as expected
    expected_starting_string = 'NNCB'
    expected_pair_insertions = {
        'CH': 'B',
        'HH': 'N',
        'CB': 'H',
        'NH': 'C',
        'HB': 'C',
        'HC': 'B',
        'HN': 'C',
        'NN': 'C',
        'BH': 'H',
        'NC': 'B',
        'NB': 'B',
        'BN': 'B',
        'BB': 'N',
        'BC': 'B',
        'CC': 'N',
        'CN': 'C'
    }
    assert actual_starting_string == expected_starting_string
    assert actual_pair_insertions == expected_pair_insertions


def test_insert_into_pairs():
    # Given some input data
    starting_string = 'NNCB'
    pair_insertions = {
        'CH': 'B',
        'HH': 'N',
        'CB': 'H',
        'NH': 'C',
        'HB': 'C',
        'HC': 'B',
        'HN': 'C',
        'NN': 'C',
        'BH': 'H',
        'NC': 'B',
        'NB': 'B',
        'BN': 'B',
        'BB': 'N',
        'BC': 'B',
        'CC': 'N',
        'CN': 'C'
    }
    count_dict = {
        'N': 2,
        'C': 1,
        'B': 1
    }

    # When the function is called
    actual_string, actual_count_dict = insert_into_pairs(starting_string, pair_insertions, count_dict)

    # Then the output is as expected
    expected_string = 'NCNBCHB'
    expected_count_dict = {
        'N': 2,
        'C': 2,
        'B': 2,
        'H': 1
    }
    assert actual_string == expected_string
    assert actual_count_dict == expected_count_dict


def test_iterate_insert_into_pairs():
    # Given some input data
    starting_string = 'NNCB'
    pair_insertions = {
        'CH': 'B',
        'HH': 'N',
        'CB': 'H',
        'NH': 'C',
        'HB': 'C',
        'HC': 'B',
        'HN': 'C',
        'NN': 'C',
        'BH': 'H',
        'NC': 'B',
        'NB': 'B',
        'BN': 'B',
        'BB': 'N',
        'BC': 'B',
        'CC': 'N',
        'CN': 'C'
    }
    number_of_iters = 4

    # When the function is called
    actual_string, actual_count_dict = iterate_insert_into_pairs(number_of_iters, starting_string, pair_insertions)

    # Then the output is as expected
    expected_string = 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'
    expected_count_dict = {
        'B': 23,
        'C': 10,
        'H': 5,
        'N': 11
    }
    assert actual_string == expected_string
    assert actual_count_dict == expected_count_dict


def test_find_most_and_least_common_delta():
    # Given some input data
    input_data = {
        'B': 1749,
        'C': 298,
        'H': 161,
        'N': 865
    }

    # When the function is called
    actual = find_most_and_least_common_delta(input_data)

    # Then the output is as expected
    expected = 1588
    assert actual == expected
