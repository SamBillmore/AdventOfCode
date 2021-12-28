from advent_of_code.day_11.solutions.day_11_puzzle_1 import DumboOctopi


def test_update_neighbours():
    # Given some input data
    input_data = [
        [ 2 , 2 , 2 , 1 , 1 ],
        [ 2 ,'f','f', 9 , 1 ],
        [ 2 ,10 , 2 , 9 , 1 ],
        [ 1 , 9 , 9 , 9 , 1 ],
        [ 1 , 1 , 1 , 1 , 1 ]
    ]
    octopi = DumboOctopi(input_data)
    row_pos = 1
    col_pos = 2

    # When the function is called
    octopi.update_neighbours(row_pos, col_pos)
    actual = octopi.energy_levels

    # Then the output is as expected
    expected = [
        [ 2 , 3 , 3 , 2 , 1 ],
        [ 2 ,'f','f',10 , 1 ],
        [ 2 ,11 , 3 ,10 , 1 ],
        [ 1 , 9 , 9 , 9 , 1 ],
        [ 1 , 1 , 1 , 1 , 1 ]
    ]
    assert actual == expected


from advent_of_code.day_11.solutions.day_11_puzzle_1 import DumboOctopi


def test_iterate_through_energy_levels_neighbours():
    # Given some input data
    input_data = [
        [ 2 , 2 , 2 , 2 , 2 ],
        [ 2 ,10 ,10 ,10 , 2 ],
        [ 2 ,10 , 2 ,10 , 2 ],
        [ 2 ,10 ,10 ,10 , 2 ],
        [ 2 , 2 , 2 , 2 , 2 ]
    ]
    octopi = DumboOctopi(input_data)

    # When the function is called
    octopi.iterate_through_energy_levels_neighbours()
    actual = octopi.energy_levels

    # Then the output is as expected
    expected = [
        [ 3 , 4 , 5 , 4 , 3 ],
        [ 4 ,'f','f','f', 4 ],
        [ 5 ,'f',10 ,'f', 5 ],
        [ 4 ,'f','f','f', 4 ],
        [ 3 , 4 , 5 , 4 , 3 ]
    ]
    assert actual == expected


def test_iterate_through_energy_levels_neighbours_complex_1():
    # Given some input data
    input_data = [
        [5,4,8,3,1,4,3,2,2,3],
        [2,7,4,5,8,5,4,7,1,1],
        [5,2,6,4,5,5,6,1,7,3],
        [6,1,4,1,3,3,6,1,4,6],
        [6,3,5,7,3,8,5,4,7,8],
        [4,1,6,7,5,2,4,6,4,5],
        [2,1,7,6,8,4,1,7,2,1],
        [6,8,8,2,8,8,1,1,3,4],
        [4,8,4,6,8,4,8,5,5,4],
        [5,2,8,3,7,5,1,5,2,6]
    ]
    octopi = DumboOctopi(input_data)

    # When the function is called
    octopi.iterate_through_energy_levels_neighbours()
    actual = octopi.energy_levels

    # Then the output is as expected
    expected = [
        [5,4,8,3,1,4,3,2,2,3],
        [2,7,4,5,8,5,4,7,1,1],
        [5,2,6,4,5,5,6,1,7,3],
        [6,1,4,1,3,3,6,1,4,6],
        [6,3,5,7,3,8,5,4,7,8],
        [4,1,6,7,5,2,4,6,4,5],
        [2,1,7,6,8,4,1,7,2,1],
        [6,8,8,2,8,8,1,1,3,4],
        [4,8,4,6,8,4,8,5,5,4],
        [5,2,8,3,7,5,1,5,2,6]
    ]
    assert actual == expected


def test_single_step():
    # Given some input data
    input_data = [
        [ 1 , 1 , 1 , 1 , 1 ],
        [ 1 , 9 , 9 , 9 , 1 ],
        [ 1 , 9 , 1 , 9 , 1 ],
        [ 1 , 9 , 9 , 9 , 1 ],
        [ 1 , 1 , 1 , 1 , 1 ]
    ]
    octopi = DumboOctopi(input_data)

    # When the function is called
    octopi.single_step()
    actual = octopi.energy_levels

    # Then the output is as expected
    expected = [
        [3,4,5,4,3],
        [4,0,0,0,4],
        [5,0,0,0,5],
        [4,0,0,0,4],
        [3,4,5,4,3]
    ]
    assert actual == expected


def test_single_step_complex():
    # Given some input data
    input_data = [
        [5,4,8,3,1,4,3,2,2,3],
        [2,7,4,5,8,5,4,7,1,1],
        [5,2,6,4,5,5,6,1,7,3],
        [6,1,4,1,3,3,6,1,4,6],
        [6,3,5,7,3,8,5,4,7,8],
        [4,1,6,7,5,2,4,6,4,5],
        [2,1,7,6,8,4,1,7,2,1],
        [6,8,8,2,8,8,1,1,3,4],
        [4,8,4,6,8,4,8,5,5,4],
        [5,2,8,3,7,5,1,5,2,6]
    ]
    octopi = DumboOctopi(input_data)

    # When the function is called
    octopi.single_step()
    actual = octopi.energy_levels

    # Then the output is as expected
    expected = [
        [6, 5, 9, 4, 2, 5, 4, 3, 3, 4],
        [3, 8, 5, 6, 9, 6, 5, 8, 2, 2],
        [6, 3, 7, 5, 6, 6, 7, 2, 8, 4],
        [7, 2, 5, 2, 4, 4, 7, 2, 5, 7],
        [7, 4, 6, 8, 4, 9, 6, 5, 8, 9],
        [5, 2, 7, 8, 6, 3, 5, 7, 5, 6],
        [3, 2, 8, 7, 9, 5, 2, 8, 3, 2],
        [7, 9, 9, 3, 9, 9, 2, 2, 4, 5],
        [5, 9, 5, 7, 9, 5, 9, 6, 6, 5],
        [6, 3, 9, 4, 8, 6, 2, 6, 3, 7]
    ]
    assert actual == expected


def test_complete_multiple_steps():
    # Given some input data
    input_data = [
        [5,4,8,3,1,4,3,2,2,3],
        [2,7,4,5,8,5,4,7,1,1],
        [5,2,6,4,5,5,6,1,7,3],
        [6,1,4,1,3,3,6,1,4,6],
        [6,3,5,7,3,8,5,4,7,8],
        [4,1,6,7,5,2,4,6,4,5],
        [2,1,7,6,8,4,1,7,2,1],
        [6,8,8,2,8,8,1,1,3,4],
        [4,8,4,6,8,4,8,5,5,4],
        [5,2,8,3,7,5,1,5,2,6]
    ]
    octopi = DumboOctopi(input_data)
    number_of_steps = 10

    # When the function is called
    octopi.complete_multiple_steps(number_of_steps)
    actual = octopi.energy_levels

    # Then the output is as expected
    expected = [
        [0,4,8,1,1,1,2,9,7,6],
        [0,0,3,1,1,1,2,0,0,9],
        [0,0,4,1,1,1,2,5,0,4],
        [0,0,8,1,1,1,1,4,0,6],
        [0,0,9,9,1,1,1,3,0,6],
        [0,0,9,3,5,1,1,2,3,3],
        [0,4,4,2,3,6,1,1,3,0],
        [5,5,3,2,2,5,2,3,5,0],
        [0,5,3,2,2,5,0,6,0,0],
        [0,0,3,2,2,4,0,0,0,0],
    ]
    assert actual == expected
