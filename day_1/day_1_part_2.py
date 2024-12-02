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
    left_values = []
    right_values = []
    with open("input_part_2.txt", "r") as infile:
        for line in infile:
            split_line = line.split()
            left_values.append(split_line[0])
            right_values.append(split_line[1])

    left_values = np.array(np.int64(left_values))
    right_values = np.array(np.int64(right_values))

    similarity = 0
    for element in left_values:
        #print(f"Elements: {element} Instances: {right_values[right_values == element]}, size: {np.size(right_values[right_values == element])}")
        similarity = similarity + (element*(right_values[element == right_values].size))
    print(similarity)
my_code()