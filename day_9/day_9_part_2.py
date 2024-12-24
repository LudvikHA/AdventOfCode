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
        if blocks[1] != -1:
            output_disk_map = output_disk_map + str(blocks[1])*blocks[0]
        else:
            output_disk_map = output_disk_map + "."*blocks[0]
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
                spaced_blocks.append((blocks, -1))
            else:
                spaced_blocks.append((blocks, ID))
                ID += 1
       
        results = []
        result_indices = []
        formatted_disk_map = np.array(spaced_blocks)
        altered_disk_map = formatted_disk_map.copy()

        file_index = np.flip(np.where(altered_disk_map[:, 1] > 0)) #Finds the index of all tuples that arent free spaces
        for index in file_index[0]:
            block = altered_disk_map[index] #Finds the value of the tuple
            length_of_block = block[0]
            free_space = np.where(altered_disk_map[:, 0] >= length_of_block)

            try:
                counter = 0
                while not free_space[0][counter] in file_index:
                    counter += 1

                altered_disk_map[free_space[0][counter]-1, 0] -= length_of_block
                results.append((block, free_space[0][counter]))
                result_indices.append(free_space[0][counter])
            except IndexError:
                pass
        print(results)

        # 009999992...333.44.5555.6666.777.888899
        # 2333133121414131402 Raw data
        #        00...111...2...333.44.5555.6666.777.888899
        #        00...111...2...333.44.5555.6666.777.888899 Formatted
        # print("00992111777.44.333....5555.6666.....8888..") desired output

        #print(altered_disk_map)
        print(ouput_processor(altered_disk_map))

my_code()
