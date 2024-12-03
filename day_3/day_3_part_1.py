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

@calculate_time
def my_code():
    mul_finder = re.compile(r"mul[(]([0-9]+),([0-9]+)[)]")
    total_sum = 0
    with open("input_part_1.txt", "r") as infile:
        for lines in infile:
            values_to_mul = re.findall(mul_finder, lines)
            for pairs in values_to_mul:
                total_sum = total_sum + int(pairs[0])*int(pairs[1])
        print(total_sum)

my_code()