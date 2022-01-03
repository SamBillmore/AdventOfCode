from advent_of_code.day_16.solutions.day_16_puzzle_1 import hex_to_literal
from advent_of_code.day_16.solutions.day_16_puzzle_2 import parse_packet_to_distinct_sub_packets, apply_all_operations


def test_parse_packet_to_distinct_sub_packets():
    # Given some input data
    input_data = '9C0141080250320F1802104A08'
    packet = hex_to_literal(input_data)

    # When the function is called
    actual = parse_packet_to_distinct_sub_packets(packet)

    # Then the output is as expected
    expected = [
        {'total_length_of_sub_packets': 80, 'operation': 'equal to', 'packet_length': 22},
        {'number_of_sub_packets': 2, 'operation': 'sum', 'packet_length': 18},
        {'value': 1, 'operation': 'literal value', 'packet_length': 11},
        {'value': 3, 'operation': 'literal value', 'packet_length': 11},
        {'number_of_sub_packets': 2, 'operation': 'product', 'packet_length': 18},
        {'value': 2, 'operation': 'literal value', 'packet_length': 11},
        {'value': 2, 'operation': 'literal value', 'packet_length': 11}
    ]
    assert actual == expected


def test_apply_all_operations_1():
    # Given some input data
    input_data = '9C0141080250320F1802104A08'
    packet = hex_to_literal(input_data)
    list_operations = parse_packet_to_distinct_sub_packets(packet)

    # When the function is called
    actual = apply_all_operations(list_operations)

    # Then the output is as expected
    expected = 1
    assert actual == expected


[{'total_length_of_sub_packets': 33, 'operation': 'sum', 'packet_length': 22}, {'value': 2, 'operation': 'literal value', 'packet_length': 11}, {'value': 4, 'operation': 'literal value', 'packet_length': 11}, {'value': 9, 'operation': 'literal value', 'packet_length': 11}, {'value': 20338968, 'operation': 'literal value', 'packet_length': 86}]
[{'total_length_of_sub_packets': 33, 'operation': 'sum', 'packet_length': 22}, {'value': 10, 'operation': 'literal value', 'packet_length': 11}, {'value': 15, 'operation': 'literal value', 'packet_length': 11}, {'value': 14, 'operation': 'literal value', 'packet_length': 11}, {'value': 24, 'operation': 'literal value', 'packet_length': 51}, {'value': 15, 'operation': 'literal value', 'packet_length': 55}]
[{'total_length_of_sub_packets': 161, 'operation': 'product', 'packet_length': 22}, {'value': 39, 'operation': 'literal value', 'packet_length': 55}, {'value': 15, 'operation': 'literal value', 'packet_length': 55}]