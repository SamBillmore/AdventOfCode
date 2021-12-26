from advent_of_code.day_8.solutions.day_8_puzzle_2 import determine_digits, find_known_digits, find_three, find_nine, find_two, find_zero, find_six, find_five, digit_lookup, sum_output_values


def test_sum_output_values():
    # Given some input data
    input_data = [
         # 1     8          9         ?         4       ?        ?         3        ?        7
        [['be', 'cfbegad', 'cbdgef', 'fgaecd', 'cgeb', 'fdcge', 'agebfd', 'fecdb', 'fabcd', 'edb'], ['fdgacbe', 'cefdb', 'cefbgd', 'gcbe']],
        [['edbfga', 'begcd', 'cbg', 'gc', 'gcadebf', 'fbgde', 'acbgfd', 'abcde', 'gfcbed', 'gfec'], ['fcgedb', 'cgb', 'dgebacf', 'gc']],
        [['fgaebd', 'cg', 'bdaec', 'gdafb', 'agbcfd', 'gdcbef', 'bgcad', 'gfac', 'gcb', 'cdgabef'], ['cg', 'cg', 'fdcagb', 'cbg']],
        [['fbegcd', 'cbd', 'adcefb', 'dageb', 'afcb', 'bc', 'aefdc', 'ecdab', 'fgdeca', 'fcdbega'], ['efabcd', 'cedba', 'gadfec', 'cb']],
        [['aecbfdg', 'fbg', 'gf', 'bafeg', 'dbefa', 'fcge', 'gcbea', 'fcaegb', 'dgceab', 'fcbdga'], ['gecf', 'egdcabf', 'bgf', 'bfgea']],
        [['fgeab', 'ca', 'afcebg', 'bdacfeg', 'cfaedg', 'gcfdb', 'baec', 'bfadeg', 'bafgc', 'acf'], ['gebdcfa', 'ecba', 'ca', 'fadegcb']],
        [['dbcfg', 'fgd', 'bdegcaf', 'fgec', 'aegbdf', 'ecdfab', 'fbedc', 'dacgb', 'gdcebf', 'gf'], ['cefg', 'dcbef', 'fcge', 'gbcadfe']],
        [['bdfegc', 'cbegaf', 'gecbf', 'dfcage', 'bdacg', 'ed', 'bedf', 'ced', 'adcbefg', 'gebcd'], ['ed', 'bcgafe', 'cdgba', 'cbgef']],
        [['egadfb', 'cdbfeg', 'cegd', 'fecab', 'cgb', 'gbdefca', 'cg', 'fgcdab', 'egfdb', 'bfceg'], ['gbdfcae', 'bgc', 'cg', 'cgb']],
        [['gcafb', 'gcf', 'dcaebfg', 'ecagb', 'gf', 'abcdeg', 'gaef', 'cafbge', 'fdbac', 'fegbdc'], ['fgae', 'cfgab', 'fg', 'bagce']]
    ]

    # When we run the function
    actual = sum_output_values(input_data)

    # Then the output is as expected
    expected = 61229
    assert actual == expected



def test_determine_digits():
    # Given some input data
    input_data = [
        ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab'], ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']
    ]

    # When we run the function
    actual = determine_digits(input_data)

    # Then the output is as expected
    expected = '5353'
    assert actual == expected


def test_find_known_digits():
    # Given some input data
    signal_patterns = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']

    # When we run the function
    actual = find_known_digits(signal_patterns)

    # Then the output is as expected
    expected = ('ab', 'eafb', 'dab', 'acedgfb')
    assert actual == expected


def test_find_three():
    # Given some input data
    signal_patterns = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
    seven = 'dab'

    # When we run the function
    actual = find_three(signal_patterns, seven)

    # Then the output is as expected
    expected = 'fbcad'
    assert actual == expected


def test_find_nine():
    # Given some input data
    signal_patterns = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
    three = 'fbcad'

    # When we run the function
    actual = find_nine(signal_patterns, three)

    # Then the output is as expected
    expected = 'cefabd'
    assert actual == expected


def test_find_zero():
    # Given some input data
    signal_patterns = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
    nine = 'cefabd'
    one = 'ab'

    # When we run the function
    actual = find_zero(signal_patterns, nine, one)

    # Then the output is as expected
    expected = 'cagedb'
    assert actual == expected


def test_find_six():
    # Given some input data
    signal_patterns = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
    zero = 'cagedb'
    nine = 'cefabd'

    # When we run the function
    actual = find_six(signal_patterns, zero, nine)

    # Then the output is as expected
    expected = 'cdfgeb'
    assert actual == expected


def test_find_five():
    # Given some input data
    signal_patterns = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
    six = 'cdfgeb'

    # When we run the function
    actual = find_five(signal_patterns, six)

    # Then the output is as expected
    expected = 'cdfbe'
    assert actual == expected


def test_find_two():
    # Given some input data
    signal_patterns = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
    zero = 'cagedb'
    one = 'ab'
    three = 'fbcad'
    four = 'eafb'
    five = 'cdfbe'
    six = 'cdfgeb'
    seven = 'dab'
    eight = 'acedgfb'
    nine = 'cefabd'

    # When we run the function
    actual = find_two(signal_patterns, zero, one, three, four, five, six, seven, eight, nine)

    # Then the output is as expected
    expected = 'gcdfa'
    assert actual == expected


def test_digit_lookup():
    # Given some input data
    digit = 'cdfeb'
    zero = 'cagedb'
    one = 'ab'
    two = 'gcdfa'
    three = 'fbcad'
    four = 'eafb'
    five = 'cdfbe'
    six = 'cdfgeb'
    seven = 'dab'
    eight = 'acedgfb'
    nine = 'cefabd'

    # When we run the function
    actual = digit_lookup(digit, zero, one, two, three, four, five, six, seven, eight, nine)

    # Then the output is as expected
    expected = '5'
    assert actual == expected
