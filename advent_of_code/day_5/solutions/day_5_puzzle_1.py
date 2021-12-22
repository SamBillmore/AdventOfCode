from advent_of_code.utils.get_data import get_data_from_txt


def data_munging(input_data):
    """
    """
    output_list = []
    for entry in input_data:
        row_list = []
        row = entry.split(' -> ')
        for pair in row:
            pair_list = []
            pair = pair.split(',')
            for item in pair:
                item = int(item)
                pair_list.append(item)
            row_list.append(tuple(pair_list))
        output_list.append(tuple(row_list))
    return output_list


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_5_data.txt"
    input_data = get_data_from_txt(filepath)
    output = data_munging(input_data)
    print(f"Final output: {output}")
