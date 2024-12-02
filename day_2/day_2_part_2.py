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
            diff = difference(single_report)
            increase = increasing(single_report)
            decrease = decreasing(single_report)

            if diff == False:
                pass
            if increase == False:
                pass
            if decrease == False:
                pass

            if diff and (increase or decrease):
                reports += 1

    print(reports)

def difference(my_array):
    #Checks if the differnce between two numbers are 1, 2 or 3. Returns
    return not (np.any((np.abs(my_array[1:] - my_array[:-1]) > 3)) or np.any((np.abs(my_array[1:] - my_array[:-1]) == 0)))

def increasing(my_array):
        #Checks if the values are increasing
        return np.all(my_array[1:] >=  my_array[:-1])

def decreasing(my_array):
        #Checks if the values are increasing
        return np.all(my_array[1:] <=  my_array[:-1])
my_code()