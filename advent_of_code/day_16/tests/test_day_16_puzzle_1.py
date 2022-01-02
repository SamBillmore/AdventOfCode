from advent_of_code.day_16.solutions.day_16_puzzle_1 import hex_to_literal, find_version_and_type, check_master_packet_contains_only_zeros, parse_packet


def test_hex_to_literal():
    # Given some input data
    input_data = 'D2FE28'

    # When the function is called
    actual = hex_to_literal(input_data)

    # Then the output is as expected
    expected = '110100101111111000101000'
    assert actual == expected


def test_find_version_and_type():
    # Given some input data
    input_data = '110100101111111000101000'

    # When the function is called
    actual = find_version_and_type(input_data)

    # Then the output is as expected
    expected = (6, 4)
    assert actual == expected


def test_check_master_packet_contains_only_zeros_true():
    # Given some input data
    input_data = '00000000000000000'

    # When the function is called
    actual = check_master_packet_contains_only_zeros(input_data)

    # Then the output is as expected
    expected = True
    assert actual == expected


def test_check_master_packet_contains_only_zeros_false():
    # Given some input data
    input_data = '00000100000000000'

    # When the function is called
    actual = check_master_packet_contains_only_zeros(input_data)

    # Then the output is as expected
    expected = False
    assert actual == expected


def test_parse_packet_1():
    # Given some input data
    input_data = 'D2FE28'
    packet = hex_to_literal(input_data)

    # When the function is called
    actual = parse_packet(packet)

    # Then the output is as expected
    expected = 6
    assert actual == expected


def test_parse_packet_2():
    # Given some input data
    input_data = '8A004A801A8002F478'
    packet = hex_to_literal(input_data)

    # When the function is called
    actual = parse_packet(packet)

    # Then the output is as expected
    expected = 16
    assert actual == expected


def test_parse_packet_3():
    # Given some input data
    input_data = '620080001611562C8802118E34'
    packet = hex_to_literal(input_data)

    # When the function is called
    actual = parse_packet(packet)

    # Then the output is as expected
    expected = 12
    assert actual == expected


def test_parse_packet_4():
    # Given some input data
    input_data = 'C0015000016115A2E0802F182340'
    packet = hex_to_literal(input_data)

    # When the function is called
    actual = parse_packet(packet)

    # Then the output is as expected
    expected = 23
    assert actual == expected


def test_parse_packet_6():
    # Given some input data
    input_data = 'A0016C880162017C3686B18A3D4780'
    packet = hex_to_literal(input_data)

    # When the function is called
    actual = parse_packet(packet)

    # Then the output is as expected
    expected = 31
    assert actual == expected
