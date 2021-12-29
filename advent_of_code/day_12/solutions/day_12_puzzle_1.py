from typing import List
from advent_of_code.utils.get_data import get_data_from_txt


EXISTING_ROUTES = []


def data_munging(input_data:List[str]) -> List[List[str]]:
    output = []
    for row in input_data:
        row_1 = row.split('-')
        row_2 = row_1[::-1]
        potential_rows = [row_1, row_2]
        for potential_row in potential_rows:
            if potential_row[0] != 'end' and potential_row [1] != 'start':
                output.append(potential_row)
    return output
    

def find_all_routes(available_edges: List[List[str]], current_route: List):
    # Find starting node
    starting_node = current_route[-1]
    # If starting_node == 'end' then append
    if starting_node == 'end':
        global EXISTING_ROUTES
        EXISTING_ROUTES.append(current_route)
        return
    # Find edges for starting node
    available_edges_from_starting_node = _find_edges_for_node(available_edges, starting_node)
    # If edges existing from starting node
    if len(available_edges_from_starting_node) > 0:
        # For each edge
        for edge in available_edges_from_starting_node:
            # Add end node to current route
            extended_current_route = current_route.copy() + [edge[1]]
            # Remove edge from available edges
            updated_available_edges = available_edges.copy()
            updated_available_edges.remove(edge)
            # Remove other edges that are now no longer possible 
            # (as not allowed to revisit lowercase nodes more than once)
            if edge[1].lower() == edge[1]:
                for available_edge in updated_available_edges:
                    if available_edge[1] == edge[1]:
                        updated_available_edges.remove(available_edge)
            # Find routes for new node
            find_all_routes(updated_available_edges, extended_current_route)
    else:
        return


def count_valid_routes(input_edges: List[List[str]]) -> List[List[str]]:
    # Reset global variable
    global EXISTING_ROUTES
    EXISTING_ROUTES = []
    
    filtered_routes = []
    start_of_route = ['start']
    find_all_routes(input_edges, start_of_route)
    for route in EXISTING_ROUTES:
        lower_case_nodes = []
        for node in route:
            if node.lower() == node:
                lower_case_nodes.append(node)
        if len(set(lower_case_nodes)) == len(lower_case_nodes):
            filtered_routes.append(route)
    return len(filtered_routes)


def _find_edges_for_node(available_edges: List[List[str]], starting_node: str) -> List:
    available_edges_from_starting_node = []
    for available_edge in available_edges:
        if available_edge[0] == starting_node:
            available_edges_from_starting_node.append(available_edge)
    return available_edges_from_starting_node
    

if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_12_data.txt"
    input_data = get_data_from_txt(filepath)
    munged_data = data_munging(input_data)
    output = count_valid_routes(munged_data)
    print(f"Final output: {output}")
