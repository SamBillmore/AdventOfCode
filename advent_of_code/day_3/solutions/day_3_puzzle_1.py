from typing import List
from advent_of_code.utils.get_data import get_binary_data


def power_consumption(data_list : List[bytes]) -> int:
    """ 
    """
    len_diagnostic_report = len(data_list)
    running_counter = []
    output_gamma_binary = []
    output_epsilon_binary = []
    for i in range(0,len(data_list[0])):
        running_counter.append(0)
    for entry in data_list:
        for i in range(0,len(entry)):
            if entry[i:i+1] == b'1':
                running_counter[i] = running_counter[i] + 1
    for i in running_counter:
        if i >= len_diagnostic_report/2:
            output_gamma_binary.append(1)
            output_epsilon_binary.append(0)
        else:
            output_gamma_binary.append(0)
            output_epsilon_binary.append(1)
    output_gamma = int(''.join(map(str, output_gamma_binary)),2)
    output_epsilon = int(''.join(map(str, output_epsilon_binary)),2)
    return output_gamma * output_epsilon    


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_3_data.bin"
    list_of_measurements = get_binary_data(filepath)
    power_usage = power_consumption(list_of_measurements)
    print(f"Final output: {power_usage}")
