from typing import List

from advent_of_code.utils.get_data import get_data_from_txt
from advent_of_code.day_12.solutions.day_12_puzzle_1 import data_munging, _find_edges_for_node


EXISTING_ROUTES = []


def find_all_routes_2(available_edges: List[List[str]], current_route: List, small_cave_flag: bool):
    global EXISTING_ROUTES
    # Find starting node
    starting_node = current_route[-1]
    # If starting_node == 'end' then append
    if starting_node == 'end':
        EXISTING_ROUTES.append(current_route)
        return
    # Find edges for starting node
    available_edges_from_starting_node = _find_edges_for_node(available_edges, starting_node)
    if starting_node == 'start':
        print(len(available_edges_from_starting_node))
    # If edges existing from starting node
    if len(available_edges_from_starting_node) > 0:
        # For each edge
        for edge in available_edges_from_starting_node:
            # Add end node to current route
            extended_current_route = current_route.copy() + [edge[1]]
            # Remove edge from available edges
            updated_available_edges = available_edges.copy()
            if small_cave_flag == True:
                lower_case_nodes = []
                for node in extended_current_route:
                    if node.lower() == node:
                        lower_case_nodes.append(node)
                if len(set(lower_case_nodes)) < len(lower_case_nodes):
                    updated_small_cave_flag = False
                else:
                    updated_small_cave_flag = small_cave_flag
            if updated_small_cave_flag == False:
                updated_available_edges.remove(edge)
                # Remove other edges that are now no longer possible 
                # (as not allowed to revisit lowercase nodes more than once)
                if edge[1].lower() == edge[1]:
                    for available_edge in updated_available_edges:
                        if available_edge[1] == edge[1]:
                            updated_available_edges.remove(available_edge)
            # Find routes for new node
            find_all_routes_2(updated_available_edges, extended_current_route, small_cave_flag)
    else:
        return

    
def count_valid_routes_2(input_edges: List[List[str]]) -> List[List[str]]:
    # Reset global variable
    global EXISTING_ROUTES
    EXISTING_ROUTES = []
    
    filtered_routes = []
    start_of_route = ['start']
    small_cave_flag = True
    find_all_routes_2(input_edges, start_of_route, small_cave_flag)
    for route in EXISTING_ROUTES:
        lower_case_nodes = []
        for node in route:
            if node.lower() == node:
                lower_case_nodes.append(node)
        if len(set(lower_case_nodes)) == len(lower_case_nodes) or len(set(lower_case_nodes)) + 1 == len(lower_case_nodes):
            filtered_routes.append(route)
    return len(set(tuple(row) for row in filtered_routes))


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_12_data.txt"
    input_data = get_data_from_txt(filepath)
    munged_data = data_munging(input_data)
    output = count_valid_routes_2(munged_data)
    print(f"Final output: {output}")
