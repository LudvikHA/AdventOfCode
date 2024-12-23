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
        disk_map = np.int64([number for number in data])
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
        reversed_disk_map = np.flip(formatted_disk_map)
        reversed_disk_map = reversed_disk_map[reversed_disk_map != "."]
        
        altered_disk_map = np.copy(formatted_disk_map)
        free_spaces = np.where(formatted_disk_map==".")[0]
        amount_of_free_spaces = len(free_spaces)
        for index_free, blocks_free in enumerate(free_spaces):
            altered_disk_map[blocks_free] = reversed_disk_map[index_free]
        altered_disk_map = altered_disk_map[:-amount_of_free_spaces]

        # print("0099811188827773336446555566..............")
        # testing = ""
        # for block_test in altered_disk_map:
        #     testing = testing + block_test
        # print(testing)

        # print("Ho",altered_disk_map)

        checksum = 0
        for index_checksum, ID_cheksum in enumerate(altered_disk_map):
            if ID_cheksum == ".":
                break
            checksum += index_checksum*int(ID_cheksum)
        print(checksum)
my_code()
