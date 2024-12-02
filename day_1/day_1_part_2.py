import time
import numpy as np

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
    left_pair = []
    right_pair = []
    with open("input.txt", "r") as infile:
        for line in infile:
            split_line = line.split()
            left_pair.append(split_line[0])
            right_pair.append(split_line[1])

    left_pair = np.sort(np.array(np.int64(left_pair)))
    right_pair = np.sort(np.array(np.int64(right_pair)))

    difference = np.sum(np.abs(left_pair-right_pair))
    print(difference)
my_code()