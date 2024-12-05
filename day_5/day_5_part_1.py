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


def convert_str(updates_unconverted: list[str]) -> list[int]:
    updates_converted = []
    for values_to_convert in updates_unconverted:
        updates_converted.append(int(values_to_convert))
    return updates_converted

@calculate_time
def my_code():
    rules_ordering = True
    rules = []
    updates = []
    with open("input_part_1.txt", "r") as infile:
        for lines in infile:
            lines = lines.strip()
            if lines == "":
                rules_ordering = False
            else:
                if rules_ordering == False:
                    appendable_unconverted = lines.split(",")
                    appendable_converted = convert_str(appendable_unconverted)
                    updates.append(appendable_converted)

                else:
                    appendable_unconverted = lines.split("|")
                    appendable_converted = convert_str(appendable_unconverted)
                    rules.append(appendable_converted)

        page_validity = True
        middle_value = []
        for page_updates in updates:
            for page_number in page_updates:
                if page_validity == True:
                    current_update_rules = [current_rules for current_rules in rules if page_number in current_rules]
                    for rule in current_update_rules:
                        try:
                            if page_updates.index(rule[0]) < page_updates.index(rule[1]):
                                page_validity = True
                            else:
                                page_validity = False
                                break
                        except ValueError:
                            pass
                else:
                    break
            if page_validity == True:
                middle_value.append(page_updates[int((len(page_updates)-1)/2)])
            page_validity = True
        print(sum(middle_value))


my_code()

