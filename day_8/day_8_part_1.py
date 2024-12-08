import time
import numpy as np
import re

# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):

        # storing time before function execution
        begin = time.time()
        
        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print(f"Total time taken in : {func.__name__} {end - begin:.6f}")

    return inner1

def blank_map(frequency: str) -> list[str]:
    #Makes a blank map with only one frequency
    blank_map = []
    new_line = ""
    with open("input_part_1.txt", "r") as infile:
        for line in infile:
            for character in line:
                if character not in f".{frequency}":
                    new_line = new_line + "."
                else:
                    new_line = new_line + character
            blank_map.append(line.strip())
    return blank_map

def update_map(coordinates: tuple[int, int], frequency: str, map: list[str]):
    new_line = ""
    for line_pos, character in enumerate(map[coordinates[0]]):
        if coordinates[1] == line_pos:
            new_line = new_line + "#"
        else:
            new_line = new_line + character
    return new_line


def print_map(map: list[str]):
    for line in map:
        print(line)


@calculate_time
def my_code():
    map = []
    with open("input_part_1.txt", "r") as infile:
        for line in infile:
            map.append(line.strip())

    row_length = len(map)
    column_length = len(map[0])
    antinode = 0

    test_map = blank_map("a")

    #Finds every frequency in the map
    for frequency_row_pos, frequency_row in enumerate(map):
        for frequency_column_pos, frequency in enumerate(frequency_row):

            #Finds the antinodes in based on the current frequency
            if frequency != ".":
                current_frequency_pos = (frequency_row_pos, frequency_column_pos)
                #Finds the postion of the given frequency
                for row_pos, row in enumerate(map):
                    for column_pos, character in enumerate(row):
                        if frequency == character and not current_frequency_pos == (row_pos, column_pos):
                            #Removes the current point of a frequency such that it dosent get repeated
                            map[frequency_row_pos] = map[frequency_row_pos].replace(frequency, "|", count=1)

                            frequency_partner = (row_pos, column_pos)
                            frequency_partner_distance = (abs(current_frequency_pos[0]-frequency_partner[0]), abs(current_frequency_pos[1]-frequency_partner[1]))

                            #Checks if the antinode of the partner is outside the current map size
                            partner_antinode_pos = (frequency_partner[0]+frequency_partner_distance[0], frequency_partner[1]+frequency_partner_distance[1])
                            current_antinode_pos = (current_frequency_pos[0]-frequency_partner_distance[0], current_frequency_pos[1]-frequency_partner_distance[1])

                            print(f"Frequency parnter pos: {frequency_partner}, Current frequency pos: {current_frequency_pos}")
                            
                            print(f"Column length: {column_length}, Row length: {row_length}")

                            if partner_antinode_pos[0] < row_length and partner_antinode_pos[1] < column_length:
                                test_map[partner_antinode_pos[0]] = update_map(partner_antinode_pos, frequency, test_map)
                                print(partner_antinode_pos, "partner")

                            if (current_antinode_pos[0] >= 0 and current_antinode_pos[1] >= 0): 
                                test_map[current_antinode_pos[0]] = update_map(current_antinode_pos, frequency, test_map)
                                print(current_antinode_pos, "current")
    print_map(test_map)
    print()

    print_map(map)
    print(antinode)

my_code()

