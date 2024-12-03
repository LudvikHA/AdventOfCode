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
            dampner = False
            single_report = np.int64(np.array(line.split()))
            report_difference = update_diff(single_report)

            diff = difference(report_difference)
            increase = increasing(report_difference)
            decrease = decreasing(report_difference)

            if diff == False:
                for index, numbers in enumerate(np.abs(report_difference)):
                    if numbers > 3 or numbers == 0:
                        dampner = True
                        #print(single_report, "before")
                        single_report = np.delete(single_report, index)
                        report_difference = update_diff(single_report)
                        diff = difference(report_difference)
                        #print(single_report, "after")
                        break

            if increase == False and dampner == False and decrease == False:
                single_report_original = single_report
                for index, numbers in enumerate(single_report):
                    try:
                        if not numbers < single_report[index+1]:
                            print(single_report, "before ince")
                            single_report = np.delete(single_report, index)
                            report_difference = update_diff(single_report)
                            print(single_report, "after ince")
                            break

                    except IndexError:
                            #If increase fails to make safe revert changes
                            single_report = single_report_original
                            report_difference = update_diff(single_report)

                #Checks decreasing if increase fails
                increase = increasing(report_difference)
                if increase == False:
                    single_report = single_report_original
                    report_difference = update_diff(single_report)
                    for index, numbers in enumerate(single_report):
                        try:
                            if not numbers > single_report[index+1]:
                                print(single_report, "before dec")
                                single_report = np.delete(single_report, index)
                                report_difference = update_diff(single_report)
                                print(single_report, "after dec")
                                single_report = single_report_original
                                report_difference = update_diff(single_report)
                                break

                        except IndexError:
                                #If increase fails to make safe revert changes
                                single_report = single_report_original
                                report_difference = update_diff(single_report)           

            diff = difference(report_difference)
            increase = increasing(report_difference)
            decrease = decreasing(report_difference)
                 


            print(f"diff: {diff}, increase: {increase}, decrease: {decrease}, dampner: {dampner}, line number: {line_number+1}, Safe: {diff == True and (increase == True or decrease == True)}")

            if diff == True and (increase == True or decrease == True):
                reports += 1

    print(reports)

def difference(diff_report):
    #Checks if the differnce between two numbers are 1, 2 or 3. 
    return not (np.any(np.abs(diff_report) > 3) or np.any(np.abs(diff_report) == 0))

def increasing(diff_report):
        #Checks if the values are increasing
        return np.all(diff_report >= 0)

def decreasing(diff_report):
        #Checks if the values are increasing
        return np.all(diff_report <= 0)
def update_diff(report):
     #Updates report_difference
     return report[1:]-report[:-1] #Contains the differences between numbers
my_code()

