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
    with open("input_part_1.txt", "r") as infile:
        data = infile.readline()
        disk_map = np.int32([number for number in data])
        ID = 0
        formatted_disk_map = []

        #Reads the disk map and formats the disk map according to specs
        for index, blocks in enumerate(disk_map):
            if index % 2 != 0:
                for free_space in range(blocks):
                    formatted_disk_map = formatted_disk_map + ["."]
            else:
                for file in range(blocks):
                    formatted_disk_map = formatted_disk_map + [ID]
                ID += 1

        #Moves the rightmost file to the first empty spaces from the left side
        formatted_disk_map = np.array(formatted_disk_map)
        altered_disk_map = np.copy(formatted_disk_map)
        complete = False
        print(formatted_disk_map)
        for index_formatted, block_component in enumerate(formatted_disk_map[::-1]):
            if complete == True:
                break
            elif block_component != ".":
                for index_altered, block_altered in enumerate(altered_disk_map):
                    if np.all(altered_disk_map[index_formatted:]=="."):
                        complete = True
                        break
                        
                    elif block_altered == ".":
                        altered_disk_map[index_altered] = block_component
                        altered_disk_map[-(index_formatted+1)] = "."

                        print(f"""
Index formatted: {index_formatted}; block component: {block_component}; 
altered_disk_map: 
{altered_disk_map}
Complete: {np.all(altered_disk_map[index_formatted:]==".")}

""")
                        break

        print("0099811188827773336446555566..............")
        testing = ""
        for block_test in altered_disk_map:
            testing = testing + block_test
        print(testing)
        
# ['9' '9' '8' '8' '8' '8' '.' '7' '7' '7' '.' '6' '6' '6' '6' '.' '5' '5'
#  '5' '5' '.' '4' '4' '.' '3' '3' '3' '.' '.' '.' '2' '.' '.' '.' '1' '1'
#  '1' '.' '.' '.' '0' '0'] reversed disk_map

# ['0' '0' '.' '.' '.' '1' '1' '1' '.' '.' '.' '2' '.' '.' '.' '3' '3' '3'
#  '.' '4' '4' '.' '5' '5' '5' '5' '.' '6' '6' '6' '6' '.' '7' '7' '7' '.'
#  '8' '8' '8' '8' '9' '9'] normal disk_map

# ['0' '0' '9' '9' '8' '1' '1' '1' '8' '8' '8' '2' '7' '7' '7' '.' '3' '3'
#  '6' '3' '4' '6' '4' '5' '5' '5' '6' '5' '6' '.' '.' '.' '.' '.' '.' '.'
#  '.' '.' '.' '.' '.' '.'] altered failed

my_code()
