from advent_of_code.day_14.solutions.day_14_puzzle_2 import create_initial_pairs_dict, update_pairs_dict, iterate_update_pairs_dict, convert_pair_dict_to_count_dict


def test_create_initial_pairs_dict():
    # Given some input data
    input_data = 'NNCB'

    # When the function is called
    actual_pairs_dict = create_initial_pairs_dict(input_data)

    # Then the output is as expected
    expected_pairs_dict = {
        'NN': 1,
        'NC': 1,
        'CB': 1
    }
    assert actual_pairs_dict == expected_pairs_dict


def test_update_pairs_dict():
    # Given some input data
    pairs_dict = {
        'NN': 1,
        'NC': 1,
        'CB': 1
    }
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

    # When the function is called
    actual_pairs_dict = update_pairs_dict(pairs_dict, pair_insertions)

    # Then the output is as expected
    expected_pairs_dict = {
        'NC': 1,
        'CN': 1,
        'NB': 1,
        'BC': 1,
        'CH': 1,
        'HB': 1
    }
    assert actual_pairs_dict == expected_pairs_dict


def test_iterate_update_pairs_dict():
    # Given some input data
    pairs_dict = {
        'NN': 1,
        'NC': 1,
        'CB': 1
    }
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
    number_of_iters = 2

    # When the function is called
    actual = iterate_update_pairs_dict(number_of_iters, pairs_dict, pair_insertions)

    # Then the output is as expected
    expected = {
        'NB': 2,
        'BC': 2,
        'CC': 1,
        'CN': 1,
        'BB': 2,
        'CB': 2,
        'BH': 1,
        'HC': 1
    }
    assert actual == expected


def test_convert_pair_dict_to_count_dict():
    # Given some input data
    input_data = {
        'NB': 2,
        'BC': 2,
        'CC': 1,
        'CN': 1,
        'BB': 2,
        'CB': 2,
        'BH': 1,
        'HC': 1
    }
    starting_string = 'NNCB'

    # When the function is called
    actual = convert_pair_dict_to_count_dict(input_data, starting_string)

    # Then the output is as expected
    expected = {
        'N': 2,
        'B': 6,
        'H': 1,
        'C': 4
    }
    assert actual == expected
