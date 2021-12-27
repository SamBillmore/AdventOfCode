from advent_of_code.day_10.solutions.day_10_puzzle_1 import check_corrupted, calculate_score


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
    actual = check_corrupted(input_data)

    # Then the output is as expected
    expected = [
        '}',
        ')',
        ']',
        ')',
        '>'
    ]
    assert actual == expected


def test_calculate_score():
    # Given some input data
    input_data = [
        '}',
        ')',
        ']',
        ')',
        '>'
    ]

    # When the function is called
    actual = calculate_score(input_data)

    # Then the output is as expected
    expected = 26397
    assert actual == expected
