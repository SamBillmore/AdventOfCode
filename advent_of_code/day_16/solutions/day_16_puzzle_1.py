from typing import Tuple

from advent_of_code.utils.get_data import get_csv_data_single_row


def hex_to_literal(input_data: str) -> str:
    binary_lookup = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    binary_output = ''
    for letter in input_data:
        binary_output = binary_output + binary_lookup[letter]
    return binary_output


def find_version_and_type(packet: str) -> Tuple[int]:
    packet_version = int(packet[:3], 2)
    packet_type = int(packet[3:6], 2)
    return packet_version, packet_type


def check_master_packet_contains_only_zeros(master_packet: str) -> bool:
    if master_packet == '':
        return True
    if int(master_packet, 2) == 0:
        return True
    return False


def parse_packet(packet: str) -> int:
    master_packet = packet
    master_packet_contains_only_zeros = check_master_packet_contains_only_zeros(master_packet)
    version_sum = 0
    while master_packet_contains_only_zeros == False:
        packet_version, packet_type = find_version_and_type(master_packet)
        version_sum = version_sum + packet_version
        master_packet = master_packet[6:]
        if packet_type == 4: # (Packet is a literal value)
            while master_packet[0] == '1':
                master_packet = master_packet[5:]
            master_packet = master_packet[5:]
        else:
            length_type = master_packet[0]
            master_packet = master_packet[1:]
            if length_type == '0':
                master_packet = master_packet[15:]
            else:
                master_packet = master_packet[11:]
        master_packet_contains_only_zeros = check_master_packet_contains_only_zeros(master_packet)
    return version_sum


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_16_data.csv"
    input_data = get_csv_data_single_row(filepath)
    input_data = input_data[0]
    packet = hex_to_literal(input_data)
    output = parse_packet(packet)
    print(f"Final output: {output}")
