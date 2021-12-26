from advent_of_code.day_9.solutions.day_9_puzzle_2 import BasinFinder, find_basin_sizes, multiply_top_three_basin_sizes


def test_get_neighbours_simple():
    # Given some input data
    height_map = [
        ['1', 1 , 9 , 9 , 9 , 4 , 3 , 2 , 1 , 0 ],
        [ 3 , 9 , 8 , 7 , 8 , 9 , 4 , 9 , 2 , 1 ],
        [ 9 , 8 , 5 , 6 , 7 , 8 , 9 , 8 , 9 , 2 ],
        [ 8 , 7 , 6 , 7 , 8 , 9 , 6 , 7 , 8 , 9 ],
        [ 9 , 8 , 9 , 9 , 9 , 6 , 5 , 6 , 7 , 8 ]
    ]
    height_map_tracker = [
        [1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ]
    start_location = (0,0)
    neighbours_to_check = []
    
    basin_finder = BasinFinder(height_map)
    basin_finder.height_map_tracker = height_map_tracker

    # When the function is called
    actual_neighbours_to_check = basin_finder.get_neighbours(start_location, neighbours_to_check)

    # Then the output is as expected
    expected_neighbours_to_check = [(1,0), (0,1)]
    expected_height_map = [
        ['1','1', 9 , 9 , 9 , 4 , 3 , 2 , 1 , 0 ],
        ['1', 9 , 8 , 7 , 8 , 9 , 4 , 9 , 2 , 1 ],
        [ 9 , 8 , 5 , 6 , 7 , 8 , 9 , 8 , 9 , 2 ],
        [ 8 , 7 , 6 , 7 , 8 , 9 , 6 , 7 , 8 , 9 ],
        [ 9 , 8 , 9 , 9 , 9 , 6 , 5 , 6 , 7 , 8 ]
    ]
    expected_height_map_tracker = [
        [1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ]
    assert actual_neighbours_to_check == expected_neighbours_to_check
    assert basin_finder.height_map == expected_height_map
    assert basin_finder.height_map_tracker == expected_height_map_tracker


def test_get_neighbours_with_nine():
    # Given some input data
    height_map = [
        ['1','1', 9 , 9 , 9 , 4 , 3 , 2 , 1 , 0 ],
        [ 3 , 9 , 8 , 7 , 8 , 9 , 4 , 9 , 2 , 1 ],
        [ 9 , 8 , 5 , 6 , 7 , 8 , 9 , 8 , 9 , 2 ],
        [ 8 , 7 , 6 , 7 , 8 , 9 , 6 , 7 , 8 , 9 ],
        [ 9 , 8 , 9 , 9 , 9 , 6 , 5 , 6 , 7 , 8 ]
    ]
    height_map_tracker = [
        [1,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ]
    start_location = (0,1)
    neighbours_to_check = [(1,0)]

    basin_finder = BasinFinder(height_map)
    basin_finder.height_map_tracker = height_map_tracker

    # When the function is called
    actual_neighbours_to_check = basin_finder.get_neighbours(start_location, neighbours_to_check)

    # Then the output is as expected
    expected_neighbours_to_check = [(1,0)]
    expected_height_map = [
        ['1','1', 9 , 9 , 9 , 4 , 3 , 2 , 1 , 0 ],
        [ 3 , 9 , 8 , 7 , 8 , 9 , 4 , 9 , 2 , 1 ],
        [ 9 , 8 , 5 , 6 , 7 , 8 , 9 , 8 , 9 , 2 ],
        [ 8 , 7 , 6 , 7 , 8 , 9 , 6 , 7 , 8 , 9 ],
        [ 9 , 8 , 9 , 9 , 9 , 6 , 5 , 6 , 7 , 8 ]
    ]
    expected_height_map_tracker = [
        [1,1,1,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ]
    assert actual_neighbours_to_check == expected_neighbours_to_check
    assert basin_finder.height_map == expected_height_map
    assert basin_finder.height_map_tracker == expected_height_map_tracker


def test_expand_current_basin():
    # Given some input data
    height_map = [
        ['1', 1 , 9 , 9 , 9 , 4 , 3 , 2 , 1 , 0 ],
        [ 3 , 9 , 8 , 7 , 8 , 9 , 4 , 9 , 2 , 1 ],
        [ 9 , 8 , 5 , 6 , 7 , 8 , 9 , 8 , 9 , 2 ],
        [ 8 , 7 , 6 , 7 , 8 , 9 , 6 , 7 , 8 , 9 ],
        [ 9 , 8 , 9 , 9 , 9 , 6 , 5 , 6 , 7 , 8 ]
    ]
    height_map_tracker = [
        [1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ]
    start_location = (0,0)

    basin_finder = BasinFinder(height_map)
    basin_finder.height_map_tracker = height_map_tracker

    # When the function is called
    basin_finder.expand_current_basin(start_location)

    # Then the output is as expected
    expected_height_map = [
        ['1','1', 9 , 9 , 9 , 4 , 3 , 2 , 1 , 0 ],
        ['1', 9 , 8 , 7 , 8 , 9 , 4 , 9 , 2 , 1 ],
        [ 9 , 8 , 5 , 6 , 7 , 8 , 9 , 8 , 9 , 2 ],
        [ 8 , 7 , 6 , 7 , 8 , 9 , 6 , 7 , 8 , 9 ],
        [ 9 , 8 , 9 , 9 , 9 , 6 , 5 , 6 , 7 , 8 ]
    ]
    expected_height_map_tracker = [
        [1,1,1,0,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ]
    assert basin_finder.height_map == expected_height_map
    assert basin_finder.height_map_tracker == expected_height_map_tracker


def test_find_basins():
    # Given some input data
    height_map = [
        [ 1 , 1 , 9 , 9 , 9 , 4 , 3 , 2 , 1 , 0 ],
        [ 3 , 9 , 8 , 7 , 8 , 9 , 4 , 9 , 2 , 1 ],
        [ 9 , 8 , 5 , 6 , 7 , 8 , 9 , 8 , 9 , 2 ],
        [ 8 , 7 , 6 , 7 , 8 , 9 , 6 , 7 , 8 , 9 ],
        [ 9 , 8 , 9 , 9 , 9 , 6 , 5 , 6 , 7 , 8 ]
    ]

    basin_finder = BasinFinder(height_map)

    # When the function is called
    basin_finder.find_basins()

    # Then the output is as expected
    expected_height_map = [
        ['1','1', 9 , 9 , 9 ,'2','2','2','2','2'],
        ['1', 9 ,'3','3','3', 9 ,'2', 9 ,'2','2'],
        [ 9 ,'3','3','3','3','3', 9 ,'4', 9 ,'2'],
        ['3','3','3','3','3', 9 ,'4','4','4', 9 ],
        [ 9 ,'3', 9 , 9 , 9 ,'4','4','4','4','4']
    ]
    assert basin_finder.height_map == expected_height_map


def test_find_basin_sizes():
    # Given some input data
    height_map = [
        ['1','1', 9 , 9 , 9 ,'2','2','2','2','2'],
        ['1', 9 ,'3','3','3', 9 ,'2', 9 ,'2','2'],
        [ 9 ,'3','3','3','3','3', 9 ,'4', 9 ,'2'],
        ['3','3','3','3','3', 9 ,'4','4','4', 9 ],
        [ 9 ,'3', 9 , 9 , 9 ,'4','4','4','4','4']
    ]

    # When the function is called
    actual = find_basin_sizes(height_map)

    # Then the output is as expected
    expected = {
        '1': 3,
        '2': 9,
        '3': 14,
        '4': 9
    }
    assert actual == expected


def test_multiply_top_three_basin_sizes():
    # Given some input data
    basin_sizes = {
        '1': 3,
        '2': 9,
        '3': 14,
        '4': 9
    }

    # When the function is called
    actual = multiply_top_three_basin_sizes(basin_sizes)

    # Then the output is as expected
    expected = 9 * 14 * 9
    assert actual == expected
