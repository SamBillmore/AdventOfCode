from typing import List
import pandas as pd

from advent_of_code.utils.get_data import get_data_from_txt


def life_support(list_binary_strings: List[str]):
    """ 
    """
    df_from_binary = create_df_from_binary(list_binary_strings)
    oxygen_df = df_from_binary.copy()
    co2_df = df_from_binary.copy()
    count = 0
    while len(oxygen_df.drop_duplicates(ignore_index=True)) > 1:
        oxygen_df = most_common_value(oxygen_df, count, 'oxygen')
        count+=1
    count = 0
    while len(co2_df.drop_duplicates(ignore_index=True)) > 1:
        co2_df = least_common_value(co2_df, count, 'co2')
        count+=1
    oxygen_value = convert_row_to_integer(oxygen_df)
    co2_value = convert_row_to_integer(co2_df)
    return oxygen_value * co2_value


def create_df_from_binary(list_binary_strings: List[str]) -> pd.DataFrame:
    """ 
    """
    data_for_df = []
    for binary_string in list_binary_strings:
        separate_binary_strings = [int(char) for char in binary_string]
        data_for_df.append(separate_binary_strings)
    return pd.DataFrame(data_for_df)


def most_common_value(dataframe: pd.DataFrame, column_header: int, calculation: str) -> pd.DataFrame:
    most_common = list(dataframe[column_header].mode())
    if len(most_common) == 1:
        return dataframe[dataframe[column_header] == most_common[0]]
    elif calculation == 'oxygen':
        return dataframe[dataframe[column_header] == 1]
    else:
        return dataframe[dataframe[column_header] == 0]


def least_common_value(dataframe: pd.DataFrame, column_header: int, calculation: str) -> pd.DataFrame:
    most_common = list(dataframe[column_header].mode())
    if len(most_common) == 1:
        if most_common[0] == 1:
            return dataframe[dataframe[column_header] == 0]
        else:
            return dataframe[dataframe[column_header] == 1]
    elif calculation == 'oxygen':
        return dataframe[dataframe[column_header] == 1]
    else:
        return dataframe[dataframe[column_header] == 0]


def convert_row_to_integer(single_row_dataframe: pd.DataFrame) -> int:
    list_values_int = single_row_dataframe.values.tolist()[0]
    return int(''.join(map(str, list_values_int)),2)


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_3_data.txt"
    list_of_measurements = get_data_from_txt(filepath)
    life_support_rating = life_support(list_of_measurements)
    print(f"Final output: {life_support_rating}")
