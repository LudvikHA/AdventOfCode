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
    finder = re.compile(r"(mul[(][0-9]+,[0-9]+[)]|don't[(][)]|do[(][)])")
    number_finder = re.compile(r"mul[(]([0-9]+),([0-9]+)[)]")
    total_sum = 0
    multiplying = True
    with open("input_part_2.txt", "r") as infile:
        for lines in infile:
            data = re.findall(finder, lines)
            for info in data:
                if info == "don't()":
                    multiplying = False
                elif info == "do()":
                    multiplying = True
                elif "mul" in info and multiplying == True:
                    numbers = re.findall(number_finder, info)
                    total_sum += int(numbers[0][0])*int(numbers[0][1])
    print(f"The total sum is {total_sum}")

my_code()
