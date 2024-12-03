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
    dont_finder = re.compile(r"don't[(][)]")
    do_finder = re.compile(r"do[(][)]")
    total_sum = 0
    with open("input_part_2.txt", "r") as infile:
        for lines in infile:
            dont_match = re.search(dont_finder, lines)
            dont_block = dont_match.span()
            #Runs before first dont is found. Runs only once
            total_sum += finding_muls(lines[:dont_block[0]])

            block_amount = re.findall(dont_finder, lines)
            for blocks in block_amount:
                #Finds do
                do_match = re.search(do_finder, lines[dont_block[1]:])
                do_block = do_match.span()

                try:
                    #Finds dont
                    dont_match = re.search(dont_finder, lines[do_block[1]:])
                    dont_block = dont_match.span()

                    #Adds all mulls
                    total_sum += finding_muls(lines[do_block[1]:dont_block[0]])
                    
                except AttributeError:
                    #Adds all mulls
                    total_sum += finding_muls(lines[do_block[1]:])











        print(total_sum)


def finding_muls(line):
    mul_finder = re.compile(r"mul[(]([0-9]+),([0-9]+)[)]")
    values_to_mul = re.findall(mul_finder, line)
    mul_sum = 0
    for pairs in values_to_mul:
        mul_sum = mul_sum + int(pairs[0])*int(pairs[1])
    return mul_sum
my_code()