from advent_of_code.day_10.solutions.day_10_puzzle_2 import check_incomplete, calculate_autocomplete_score


def test_check_corrupted():
    # Given some input data
    input_data = [
        '[({(<(())[]>[[{[]{<()<>>',
        '[(()[<>])]({[<{<<[]>>(',
        '{([(<{}[<>[]}>{[]{[(<()>',
        '(((({<>}<{<{<>}{[]{[]{}',
        '[[<[([]))<([[{}[[()]]]',
        '[{[{({}]{}}([{[{{{}}([]',
        '{<[[]]>}<{[{[{[]{()[[[]',
        '[<(<(<(<{}))><([]([]()',
        '<{([([[(<>()){}]>(<<{{',
        '<{([{{}}[<[[[<>{}]]]>[]]'
    ]

    # When the function is called
    actual = check_incomplete(input_data)

    # Then the output is as expected
    expected = [
        '}}]])})]',
        ')}>]})',
        '}}>}>))))',
        ']]}}]}]}>',
        '])}>'
    ]
    assert actual == expected


def test_calculate_syntax_checker_score():
    # Given some input data
    input_data = [
        '}}]])})]',
        ')}>]})',
        '}}>}>))))',
        ']]}}]}]}>',
        '])}>'
    ]

    # When the function is called
    actual = calculate_autocomplete_score(input_data)

    # Then the output is as expected
    expected = 288957
    assert actual == expected
