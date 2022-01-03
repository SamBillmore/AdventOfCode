from typing import Dict, List

from advent_of_code.utils.get_data import get_csv_data_single_row
from advent_of_code.day_16.solutions.day_16_puzzle_1 import hex_to_literal, check_master_packet_contains_only_zeros, find_version_and_type


def _lookup_packet_type(packet_type_id: int) -> str:
    type_lookup_dict = {
        0: 'sum',
        1: 'product',
        2: 'minimum',
        3: 'maximum',
        4: 'literal value',
        5: 'greater than',
        6: 'less than',
        7: 'equal to'
    }
    return type_lookup_dict[packet_type_id]


def parse_packet_to_distinct_sub_packets(packet: str) -> List[Dict]:
    master_packet = packet
    list_distinct_packets = []
    master_packet_contains_only_zeros = check_master_packet_contains_only_zeros(master_packet)
    while master_packet_contains_only_zeros == False:
        _, packet_type = find_version_and_type(master_packet)
        distinct_packet_dict = {}
        distinct_packet = master_packet[:6]
        master_packet = master_packet[6:]
        if packet_type == 4: # (Packet is a literal value)
            literal_value_binary = ''
            while master_packet[0] == '1':
                distinct_packet = distinct_packet + master_packet[:5]
                literal_value_binary = literal_value_binary + master_packet[1:5]
                master_packet = master_packet[5:]
            distinct_packet = distinct_packet + master_packet[:5]
            literal_value_binary = literal_value_binary + master_packet[1:5]
            master_packet = master_packet[5:]
            distinct_packet_dict['value'] = int(literal_value_binary, 2)
        else:
            distinct_packet = distinct_packet + master_packet[0]
            length_type = master_packet[0]
            master_packet = master_packet[1:]
            if length_type == '0':
                distinct_packet = distinct_packet + master_packet[:15]
                distinct_packet_dict['total_length_of_sub_packets'] = int(master_packet[:15], 2)
                master_packet = master_packet[15:]
            else:
                distinct_packet = distinct_packet + master_packet[:11]
                distinct_packet_dict['number_of_sub_packets'] = int(master_packet[:11], 2)
                master_packet = master_packet[11:]
        distinct_packet_dict['operation'] = _lookup_packet_type(packet_type)
        distinct_packet_dict['packet_length'] = len(distinct_packet)
        list_distinct_packets.append(distinct_packet_dict)
        master_packet_contains_only_zeros = check_master_packet_contains_only_zeros(master_packet)
    return list_distinct_packets


def _calculate_value(operation: str, values: List[str]) -> int:
    if operation == 'sum':
        return sum(values)
    if operation == 'product':
        output = 1
        for value in values:
            output = output * value
        return output
    if operation == 'minimum':
        return min(values)
    if operation == 'maximum':
        return max(values)
    if operation == 'greater than':
        if values[0] > values[1]:
            return 1
        else:
            return 0
    if operation == 'less than':
        if values[0] < values[1]:
            return 1
        else:
            return 0
    if operation == 'equal to':
        if values[0] == values[1]:
            return 1
        else:
            return 0



def _apply_single_iteration_of_operations(list_operations: List) -> List:
    output_list_operations = []
    for index in range(len(list_operations) - 1, -1, -1):
        if 'value' not in list_operations[index].keys() and 'value' in list_operations[index + 1].keys():
            new_dict = {}
            values = []
            total_length = 0
            if 'number_of_sub_packets' in list_operations[index].keys():
                for count in range(1, list_operations[index]['number_of_sub_packets'] + 1):
                    values.append(list_operations[index + count]['value'])
                    total_length += list_operations[index + count]['packet_length']
            if 'total_length_of_sub_packets' in list_operations[index].keys():
                count = 1
                while total_length < list_operations[index]['total_length_of_sub_packets']:
                    values.append(list_operations[index + count]['value'])
                    total_length = total_length + list_operations[index + count]['packet_length']
                    count += 1
                count = count - 1
            new_value = _calculate_value(list_operations[index]['operation'], values)
            new_dict['value'] = new_value
            new_dict['operation'] = 'literal value'
            new_dict['packet_length'] = total_length + list_operations[index]['packet_length']
            output_list_operations = list_operations[:index]
            output_list_operations.append(new_dict)
            if index + count < len(list_operations) - 1:
                output_list_operations = output_list_operations + list_operations[index + count + 1:]
            return output_list_operations


def apply_all_operations(list_operations: List) -> int:
    while len(list_operations) > 1:
        list_operations = _apply_single_iteration_of_operations(list_operations)
    return list_operations[0]['value']


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_16_data.csv"
    input_data = get_csv_data_single_row(filepath)
    input_data = input_data[0]
    packet = hex_to_literal(input_data)
    list_operations = parse_packet_to_distinct_sub_packets(packet)
    output = apply_all_operations(list_operations)
    print(f"Final output: {output}")
