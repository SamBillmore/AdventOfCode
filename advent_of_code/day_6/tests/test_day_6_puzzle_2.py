from advent_of_code.day_6.solutions.day_6_puzzle_2 import iterate_fish_version_2


def test_iterate_fish_version_2():
    # Given some input data
    fish_data = [0,1,2,3,4,5]
    iterations = 9
    # [6,0,1,2,3,4,8]
    # [5,6,0,1,2,3,7,8]
    # [4,5,6,0,1,2,6,7,8]
    # [3,4,5,6,0,1,5,6,7,8]
    # [2,3,4,5,6,0,4,5,6,7,8]
    # [1,2,3,4,5,6,3,4,5,6,7,8]
    # [0,1,2,3,4,5,2,3,4,5,6,7]
    # [6,0,1,2,3,4,1,2,3,4,5,6,8]
    # [5,6,0,1,2,3,0,1,2,3,4,5,7,8]

    # When we run the funtion
    actual = iterate_fish_version_2(fish_data, iterations)

    # Then the output is as expected
    expected = 14
    assert actual == expected


from advent_of_code.day_6.solutions.day_6_puzzle_1 import single_fish_iteration
def test_run():
    iterations = 30
    fish_data = [1,1,2,3,3,4]
    print(f'\n')
    for i in range(0,iterations,1):
        fish_data = single_fish_iteration(fish_data)
        fish_data.sort()
        print(f'# {i + 1}: {fish_data}')
