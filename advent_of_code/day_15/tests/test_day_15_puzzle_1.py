from advent_of_code.day_15.solutions.day_15_puzzle_1 import create_graph_from_input, calculate_shortest_path


def test_calculate_shortest_path():
    # Given some input data
    risk_map = [
        [1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
        [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
        [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
        [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
        [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
        [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
        [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
        [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
        [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
        [2, 3, 1, 1, 9, 4, 4, 5, 8, 1]
    ]
    graph = create_graph_from_input(risk_map)
    start_point = (0,0)
    end_point = (len(risk_map) - 1, len(risk_map[0]) - 1)

    # When the function is called
    actual = calculate_shortest_path(graph, start_point, end_point)

    # Then the output is as expected
    expected = 40
    assert actual == expected


def test_template():
    # Given some input data
    input_data = ''

    # When the function is called
    actual = ''

    # Then the output is as expected
    expected = ''
    assert actual == expected
