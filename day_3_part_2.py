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
            do_blocks = re.split(do_finder, lines)
            print(do_blocks)
            for blocks in do_blocks:
                dont_match = re.search(dont_finder, blocks)
                if dont_match == None:
                    total_sum += finding_muls(blocks)
                else:
                    dont_block = dont_match.span()
                    # print(dont_block[0])
                    # print(blocks[:dont_block[0]])
                    total_sum += finding_muls(blocks[:dont_block[0]])
        print(total_sum)


def finding_muls(line):
    mul_finder = re.compile(r"mul[(]([0-9]+),([0-9]+)[)]")
    values_to_mul = re.findall(mul_finder, line)
    mul_sum = 0
    for pairs in values_to_mul:
        mul_sum = mul_sum + int(pairs[0])*int(pairs[1])
    return mul_sum
my_code()
#Last value 83942127