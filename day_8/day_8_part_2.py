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


def convert_str(updates_unconverted: list[str]) -> list[int]:
    updates_converted = []
    for values_to_convert in updates_unconverted:
        updates_converted.append(int(values_to_convert))
    return updates_converted

@calculate_time
def my_code():
    with open("input_part_2.txt", "r") as infile:
        pass
my_code()
