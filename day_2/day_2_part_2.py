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
    with open("input_part_2.txt", "r") as infile:
        for line_number, line in enumerate(infile):
            single_report = np.int64(line.split())
            report_difference = single_report[1:]-single_report[:-1]

            diff = difference(report_difference)
            increase = increasing(report_difference)
            decrease = decreasing(report_difference)

            #Difference can be used to find decreasing and increasing. 
            #If all numbers negative then decreasing. 
            #If all numbers positive increasing
            dampner = False #True if a value has been removed

            #Removes the first instance of diff that that is not 1, 2, 3
            if diff == False and dampner == False:    
                for index, numbers in enumerate(np.abs(report_difference)):
                    if numbers > 3 or numbers == 0:
                        #print(report_difference, "before")
                        single_report = np.delete(single_report, index)
                        report_difference = single_report[1:]-single_report[:-1]
                        #print(report_difference, "after")
                        diff = difference(report_difference)
                        dampner = True
                        break
                    
            if increase == False and dampner == False and decrease == False:
                for index, numbers in enumerate(report_difference):
                    if numbers < 0:
                        report_difference = np.delete(report_difference, index)
                        increase = increasing(report_difference)
                        dampner = True
                        if increase == False:
                            report_difference = np.insert(report_difference, index, numbers)
                            dampner = False
                        break
                             
            if decrease == False and dampner == False and increase == False:
                for index, numbers in enumerate(report_difference):
                    if numbers > 0:
                        report_difference = np.delete(report_difference, index)
                        decrease = decreasing(report_difference)
                        dampner = True
                        if decrease == False:
                            report_difference = np.insert(report_difference, index, numbers)
                            dampner = False
                        break

            print(f"diff: {diff}, increase: {increase}, decrease: {decrease}, dampner: {dampner}, line number: {line_number}, Safe: {diff == True and (increase == True or decrease == True)}")

            if diff == True and (increase == True or decrease == True):
                reports += 1

    print(reports)

def difference(diff_report):
    #Checks if the differnce between two numbers are 1, 2 or 3. 
    return (not np.any(np.abs(diff_report) > 3)) or (not np.any(np.abs(diff_report) == 0))

def increasing(diff_report):
        #Checks if the values are increasing
        return np.all(diff_report >= 0)

def decreasing(diff_report):
        #Checks if the values are increasing
        return np.all(diff_report <= 0)
my_code()