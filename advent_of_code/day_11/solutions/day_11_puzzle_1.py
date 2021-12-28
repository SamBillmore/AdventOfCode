from typing import List

from advent_of_code.utils.get_data import get_data_from_txt
from advent_of_code.day_9.solutions.day_9_puzzle_1 import data_munging


class DumboOctopi():

    def __init__(self, energy_levels: List[List[int]]):
        self.energy_levels = energy_levels
        self.flash_count = 0

    def complete_multiple_steps(self, number_of_steps: int):
        for _ in range(0,number_of_steps):
            self.single_step()

    def single_step(self):
        self.iterate_through_energy_levels_add_one_energy()
        max_board_value = self.iterate_through_energy_levels_max_board_value()
        while max_board_value > 9:
            self.iterate_through_energy_levels_neighbours()
            max_board_value = self.iterate_through_energy_levels_max_board_value()
        self.iterate_through_energy_levels_replace_strings()

    def iterate_through_energy_levels_max_board_value(self):
        max_board_value = 0
        for row in self.energy_levels:
            for energy_val in row:
                if type(energy_val) == int:
                    if energy_val > max_board_value:
                        max_board_value = energy_val
        return max_board_value
        
    def iterate_through_energy_levels_replace_strings(self):
        for row_pos, row in enumerate(self.energy_levels):
            for col_pos, energy_val in enumerate(row):
                if energy_val == 'f':
                    self.energy_levels[row_pos][col_pos] = 0

    def iterate_through_energy_levels_add_one_energy(self):
        for row_pos, row in enumerate(self.energy_levels):
            for col_pos, energy_val in enumerate(row):
                self.energy_levels[row_pos][col_pos] = energy_val + 1

    def iterate_through_energy_levels_neighbours(self):
        for row_pos, row in enumerate(self.energy_levels):
            for col_pos, energy_val in enumerate(row):
                if type(energy_val) == int:
                    if energy_val > 9:
                        self.flash_count = self.flash_count + 1
                        self.energy_levels[row_pos][col_pos] = 'f'
                        self.update_neighbours(row_pos, col_pos)

    def update_neighbours(self, row_pos: int, col_pos: int):
        neighbour_positions = self.find_neighbours(row_pos, col_pos)
        for neighbour_pos in neighbour_positions:
            neighbour_row = neighbour_pos[0]
            neighbour_col = neighbour_pos[1]
            neighbour_value = self.energy_levels[neighbour_row][neighbour_col]
            if type(neighbour_value) == int:
                self.energy_levels[neighbour_row][neighbour_col] = neighbour_value + 1

    def find_neighbours(self, row_pos: int, col_pos: int):
        neighbour_positions = []
        max_row_pos = len(self.energy_levels) - 1
        max_col_pos = len(self.energy_levels[0]) - 1
        possible_neighbour_positions = [
            (row_pos - 1, col_pos - 1),
            (row_pos - 1, col_pos),
            (row_pos - 1, col_pos + 1),
            (row_pos,     col_pos - 1),
            (row_pos,     col_pos + 1),
            (row_pos + 1, col_pos - 1),
            (row_pos + 1, col_pos),
            (row_pos + 1, col_pos + 1)
        ]
        for neighbour_pos in possible_neighbour_positions:
            if neighbour_pos[0] >= 0 and neighbour_pos[1] >= 0 and \
            neighbour_pos[0] <= max_row_pos and neighbour_pos[1] <= max_col_pos:
                neighbour_positions.append(neighbour_pos)
        return neighbour_positions


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_11_data.txt"
    input_data = get_data_from_txt(filepath)
    munged_data = data_munging(input_data)
    octopi = DumboOctopi(munged_data)
    octopi.complete_multiple_steps(100)
    output = octopi.flash_count
    print(f"Final output: {output}")
