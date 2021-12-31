from typing import List

from advent_of_code.utils.get_data import get_data_from_txt
from advent_of_code.day_9.solutions.day_9_puzzle_1 import data_munging
from advent_of_code.day_15.solutions.day_15_puzzle_1 import create_graph_from_input, calculate_shortest_path


def create_full_risk_map(risk_map: List[List[int]]) -> List[List[int]]:
    list_new_blocks = []
    full_risk_map = []
    for i in range(0,10):
        new_block = [[x + i if x + i <= 9 else x + i - 9 for x in row] for row in risk_map]
        list_new_blocks.append(new_block)
    for i in range(0,5):
        output_row_of_blocks = list_new_blocks[i]
        for j in range(1,5):
            output_row_of_blocks = [a + b for a, b in zip(output_row_of_blocks, list_new_blocks[i + j])]
        full_risk_map = full_risk_map + output_row_of_blocks
    return full_risk_map


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_15_data.txt"
    input_data = get_data_from_txt(filepath)
    risk_map = data_munging(input_data)
    full_risk_map = create_full_risk_map(risk_map)
    graph = create_graph_from_input(full_risk_map)
    start_point = (0,0)
    end_point = (len(full_risk_map) - 1, len(full_risk_map[0]) - 1)
    output = calculate_shortest_path(graph, start_point, end_point)
    print(f"Final output: {output}")
