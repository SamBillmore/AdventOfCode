from advent_of_code.utils.get_data import get_data_from_txt

# for i in 100:
    # Add one to each octopus
    # max_board_value = max(max(row))
    # While max_board_value >= 9 (i.e. while 9+s are on the board)
        # Iterate through board
            # If cell == 9+
                # For each neighbour:
                    # If neighbour is not a string:
                        # Add one to each neighbour
                # mark as string
        # max_board_value = max(max(row))
    # Replace strings with 0


if __name__ == "__main__":
    filepath = "./advent_of_code/data/day_11_data.txt"
    input_data = get_data_from_txt(filepath)
    
    output = ''
    print(f"Final output: {output}")
