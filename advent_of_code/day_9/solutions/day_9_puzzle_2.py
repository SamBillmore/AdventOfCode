from typing import Dict, List, Tuple

from advent_of_code.utils.get_data import get_data_from_txt
from advent_of_code.day_9.solutions.day_9_puzzle_1 import data_munging


class BasinFinder():

    def __init__(self, height_map: List[List[int]]):
        self.height_map = height_map
        self.height_map_tracker = [[0 for x in row] for row in height_map]

    def find_basins(self):
        """
        Iterate horizontally, then vertically through non-completed heights on tracker
        Mark as complete on tracker
        If not nine:
            Mark as part of next basin
            expand basin
        """
        basin_counter = 1
        start_position = (0,0)
        while start_position is not None:
            start_row = start_position[0]
            start_col = start_position[1]
            self.mark_tracker_complete(start_position)
            if self.height_map[start_row][start_col] != 9:
                print(f'Expanding basin for: {start_position}. Max rows = {len(self.height_map)}')
                self.height_map[start_row][start_col] = str(basin_counter)
                self.expand_current_basin(start_position)
                basin_counter += 1
            start_position = self.find_next_start_position()

    def find_next_start_position(self):
        """
        """
        for row_count, row in enumerate(self.height_map_tracker):
            for col_count, tracker_value in enumerate(row):
                if tracker_value == 0:
                    return (row_count, col_count)
        return None

    def expand_current_basin(self, starting_position_row_col: Tuple[int]):
        """
        # Expand current basin (while loop)
        check neighbours
            if any neighbours are not 9 then 
                mark neighbours the same
                Add to list of neighbours to check
            if neighbours are 9 then mark as complete on tracker
        Mark current location as complete on tracker
        Move to next on list of neighbours to check
        """
        neighbours_to_check = self.get_neighbours(starting_position_row_col, [])
        while len(neighbours_to_check) > 0:
            self.get_neighbours(neighbours_to_check[0], neighbours_to_check)
            self.mark_tracker_complete(neighbours_to_check[0])
            neighbours_to_check = neighbours_to_check[1:]

    def get_neighbours(self, starting_position_row_col: Tuple[int], neighbours_to_check: List[Tuple[int]]):
        """
        check neighbours
        if any neighbours are not 9 then 
            mark neighbours the same
            add to list of neighbours to check
        if neighbours are 9 then mark as complete on tracker
        """
        count_row = starting_position_row_col[0]
        count_col = starting_position_row_col[1]
        start_val = self.height_map[count_row][count_col]
        max_row = len(self.height_map) - 1
        max_col = len(self.height_map[0]) - 1

        if count_row > 0:
            neighbours_to_check = self.process_neighbour(count_row - 1, count_col, start_val, neighbours_to_check)
        if count_row < max_row:
            neighbours_to_check = self.process_neighbour(count_row + 1, count_col, start_val, neighbours_to_check)
        if count_col > 0:
            neighbours_to_check = self.process_neighbour(count_row, count_col - 1, start_val, neighbours_to_check)
        if count_col < max_col:
            neighbours_to_check = self.process_neighbour(count_row, count_col + 1, start_val, neighbours_to_check)
        return neighbours_to_check

    def process_neighbour(self, row_pos: int, col_pos: int, start_val: str, neighbours_to_check: List[Tuple[int]]):
        if self.height_map[row_pos][col_pos] != 9:
            if type(self.height_map[row_pos][col_pos]) == int:
                neighbours_to_check.append((row_pos, col_pos))
            self.height_map[row_pos][col_pos] = start_val
        else:
            self.mark_tracker_complete((row_pos, col_pos))
        return neighbours_to_check

    def mark_tracker_complete(self, position: Tuple[int]):
        row_pos = position[0]
        col_pos = position[1]
        self.height_map_tracker[row_pos][col_pos] = 1


def find_basin_sizes(height_map_with_basins: List) -> Dict:
    output_dict = {}
    for row in height_map_with_basins:
        for basin_value in row:
            if basin_value != 9:
                if basin_value in output_dict.keys():
                    output_dict[basin_value] = output_dict[basin_value] + 1
                else:
                    output_dict[basin_value] = 1
    return output_dict


def multiply_top_three_basin_sizes(basin_sizes: Dict) -> int:
    sorted_basin_sizes = list(basin_sizes.values())
    sorted_basin_sizes.sort(reverse=True)
    return sorted_basin_sizes[0] * sorted_basin_sizes[1] * sorted_basin_sizes[2]


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_9_data.txt"
    input_data = get_data_from_txt(filepath)
    height_map = data_munging(input_data)
    basin_finder = BasinFinder(height_map)
    basin_finder.find_basins()
    basin_sizes = find_basin_sizes(basin_finder.height_map)
    output = multiply_top_three_basin_sizes(basin_sizes)
    print(f"Final output: {output}")
