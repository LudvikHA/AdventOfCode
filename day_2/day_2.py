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
    reports = 0
    with open("input_part_1.txt", "r") as infile:
        for line in infile:
            single_report = np.int64(line.split())
            #Checks if the differnce between two numbers are 1, 2 or 3. Returns
            difference = not (np.any((np.abs(single_report[1:] - single_report[:-1]) > 3)) or np.any((np.abs(single_report[1:] - single_report[:-1]) == 0)))
            #Checks if the values are increasing
            increasing = np.all(single_report[1:] >=  single_report[:-1])
            #Checks if the values are decreasing
            decreasing = np.all(single_report[1:] <=  single_report[:-1])

            if difference and (increasing or decreasing):
                reports += 1
    print(reports)
my_code()