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
            safety = [True, True] #Index 0 represents True if change is less than 3, and [1] represents increasing or decreasing
            for index, element in enumerate(single_report):
                try: 
                    if abs(element - single_report[index+1]) < 3:
                        safety[0] = True
                    else:
                        safety[0] = False
                except:
                    pass

                if safety[1] == True:
                    if single_report[element > single_report].size == 0:
                        print("Increasing..")
                        safety[1] = True 
                    else:
                        safety[1] = False 

                    if single_report[element < single_report].size == 0:
                        print("Decreasing..")
                        safety[1] = True 
                    else:
                        safety[1] = False

            if sum(safety) == 2:
                reports += 1
    print(reports)


my_code()