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

def ouput_processor(disk_map):
    output_disk_map = ""
    for index, blocks in enumerate(disk_map):
        if isinstance(blocks, dict):
            for i in range(list(blocks.keys())[0]):
                output_disk_map = output_disk_map + str(list(blocks.values())[0])
        else:
            output_disk_map = output_disk_map + "."*blocks
    return output_disk_map

@calculate_time
def my_code():
    with open("input_part_example.txt", "r") as infile:
        data = infile.readline()
        disk_map = np.int64([number for number in data])
        ID = 0

        #Reads the disk map and formats the disk map according to specs
        spaced_blocks = []
        for index, blocks in enumerate(disk_map):
            if index % 2 != 0:
                spaced_blocks.append({blocks:"."})
            else:
                spaced_blocks.append({blocks:ID})
                ID += 1

        formatted_disk_map = np.array(spaced_blocks)
        altered_disk_map = formatted_disk_map[1:].copy()
        length_disk_map = len(formatted_disk_map)

        print(altered_disk_map)

        file_disk_map = formatted_disk_map[0:length_disk_map:2]
        free_disk_map = formatted_disk_map[1:length_disk_map:2]
        rev_file_disk_map = np.flip(file_disk_map)

        print(free_disk_map)

        modifier = 0
        for index, blocks in enumerate(rev_file_disk_map):
            file_block_len = list(blocks.keys())[0]
            free_space = np.where(free_disk_map >= file_block_len)

            try:
                #print(free_space)
                first_free_space = free_space[0][0]
                #print(free_disk_map[first_free_space] - file_block_len, "Update", "blocks", blocks)
                free_disk_map[first_free_space] -= file_block_len
                
                altered_disk_map[first_free_space+modifier] = free_disk_map[first_free_space]
                altered_disk_map = np.insert(altered_disk_map, first_free_space+modifier, blocks)
                
                print(f"Output: {ouput_processor(altered_disk_map)}")

            except IndexError:
                pass

        # 009999992...333.44.5555.6666.777.888899
        # 2333133121414131402 Raw data
        #        0099.777244.2...333.44.5555.6666.777.888899
        #        00...111...2...333.44.5555.6666.777.888899 Formatted
        # print("00992111777.44.333....5555.6666.....8888..") desired output

        print(altered_disk_map)
        ouput_processor(altered_disk_map)

my_code()
