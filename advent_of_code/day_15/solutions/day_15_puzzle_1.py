import networkx as nx
from typing import List, Tuple

from advent_of_code.utils.get_data import get_data_from_txt
from advent_of_code.day_9.solutions.day_9_puzzle_1 import data_munging


def create_graph_from_input(risk_map: List[List[int]]):
    G = nx.DiGraph()
    for row_index, row in enumerate(risk_map):
        for col_index, value in enumerate(row):
            # Add horizontal edges
            if col_index > 0:
                left_pos = (row_index, col_index - 1)
                right_pos = (row_index, col_index)
                G.add_edge(left_pos, right_pos, weight = risk_map[row_index][col_index])
                G.add_edge(right_pos, left_pos, weight = risk_map[row_index][col_index - 1])
            # Add vertical edges
            if row_index > 0:
                upper_pos = (row_index - 1, col_index)
                lower_pos = (row_index, col_index)
                G.add_edge(upper_pos, lower_pos, weight = risk_map[row_index][col_index])
                G.add_edge(lower_pos, upper_pos, weight = risk_map[row_index - 1][col_index])
    return G


def calculate_shortest_path(graph: nx.DiGraph, start_point: Tuple[int], end_point: Tuple[int]) -> int:
    return nx.shortest_path_length(graph, source=start_point, target=end_point, weight='weight')


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_15_data.txt"
    input_data = get_data_from_txt(filepath)
    risk_map = data_munging(input_data)
    graph = create_graph_from_input(risk_map)
    start_point = (0,0)
    end_point = (len(risk_map) - 1, len(risk_map[0]) - 1)
    output = calculate_shortest_path(graph, start_point, end_point)
    print(f"Final output: {output}")
