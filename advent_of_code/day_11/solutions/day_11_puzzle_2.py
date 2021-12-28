from typing import List

from advent_of_code.utils.get_data import get_data_from_txt
from advent_of_code.day_9.solutions.day_9_puzzle_1 import data_munging
from advent_of_code.day_11.solutions.day_11_puzzle_1 import DumboOctopi


class DumboOctopiExtended(DumboOctopi):

    def __init__(self, energy_levels: List[List[int]]):
        super().__init__(energy_levels)

    def find_all_octopi_flash(self):
        all_octopi_flash = False
        count = 0
        num_octopi = sum([sum([1 for x in row]) for row in self.energy_levels])
        while all_octopi_flash is False:
            previous_total_flash = self.flash_count
            self.single_step()
            count += 1
            if self.flash_count - previous_total_flash == num_octopi:
                all_octopi_flash = True
        return count


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_11_data.txt"
    input_data = get_data_from_txt(filepath)
    munged_data = data_munging(input_data)
    octopi = DumboOctopiExtended(munged_data)
    output = octopi.find_all_octopi_flash()
    print(f"Final output: {output}")
