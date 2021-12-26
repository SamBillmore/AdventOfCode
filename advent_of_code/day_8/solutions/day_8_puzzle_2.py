from typing import List, Tuple
from advent_of_code.utils.get_data import get_data_from_txt
from advent_of_code.day_8.solutions.day_8_puzzle_1 import data_munging


def sum_output_values(input_data: List) -> int:
    running_sum = 0
    for row_data in input_data:
        running_sum = running_sum + int(determine_digits(row_data))
    return running_sum


def determine_digits(row_data: List) -> str:
    """
    """
    signal_patterns = row_data[0]
    four_digit_output = row_data[1]

    one, four, seven, eight = find_known_digits(signal_patterns)
    three = find_three(signal_patterns, seven)
    nine = find_nine(signal_patterns, three)
    zero = find_zero(signal_patterns, nine, one)
    six = find_six(signal_patterns, zero, nine)
    five = find_five(signal_patterns, six)
    two = find_two(signal_patterns, zero, one, three, four, five, six, seven, eight, nine)

    output = ''
    for digit in four_digit_output:
        output = output + digit_lookup(digit, zero, one, two, three, four, five, six, seven, eight, nine)
    return output


def digit_lookup(digit: str, zero: str, one: str, two: str, three: str, four: str, five: str, six: str, seven: str, eight: str, nine: str) -> str:
    possible_digits = [zero, one, two, three, four, five, six, seven, eight, nine]
    digit_set = set(x for x in digit)
    for count, possible_digit in enumerate(possible_digits):
        possible_digit_set = set(x for x in possible_digit)
        if digit_set == possible_digit_set:
            return str(count)


def find_two(signal_patterns: List, zero: str, one: str, three: str, four: str, five: str, six: str, seven: str, eight: str, nine: str) -> str:
    other_digits = [zero, one, three, four, five, six, seven, eight, nine]
    for signal in signal_patterns:
        if signal not in other_digits:
            return signal


def find_five(signal_patterns: List, six: str) -> str:
    six_set = set(x for x in six)
    for signal in signal_patterns:
        if len(signal) == 5:
            signal_set = set(x for x in signal)
            if len(six_set.difference(signal_set)) == 1:
                return signal


def find_six(signal_patterns: List, zero: str, nine: str) -> str:
    for signal in signal_patterns:
        if len(signal) == 6:
            if signal != zero:
                if signal != nine:
                    return signal


def find_zero(signal_patterns: List, nine: str, one: str) -> str:
    nine_set = set(x for x in nine)
    one_set = set(x for x in one)
    for signal in signal_patterns:
        if len(signal) == 6:
            signal_set = set(x for x in signal)
            if len(signal_set.difference(nine_set)) == 1:
                if len(one_set.difference(signal_set)) == 0:
                    return signal


def find_nine(signal_patterns:List, three: str) -> str:
    three_set = set(x for x in three)
    for signal in signal_patterns:
        if len(signal) == 6:
            signal_set = set(x for x in signal)
            if len(signal_set.difference(three_set)) == 1:
                return signal


def find_three(signal_patterns: List, seven: str) -> str:
    seven_set = set(x for x in seven)
    for signal in signal_patterns:
        if len(signal) == 5:
            signal_set = set(x for x in signal)
            if len(signal_set.difference(seven_set)) == 2:
                return signal


def find_known_digits(signal_patterns: List) -> Tuple[str]:
    # Known digits
    for signal in signal_patterns:
        if len(signal) == 2:
            one = signal
        elif len(signal) ==  3:
            seven = signal
        elif len(signal) == 4:
            four = signal
        elif len(signal) == 7:
            eight = signal
    return one, four, seven, eight


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_8_data.txt"
    input_data = get_data_from_txt(filepath)
    segment_data = data_munging(input_data)
    output = sum_output_values(segment_data)
    print(f"Final output: {output}")
