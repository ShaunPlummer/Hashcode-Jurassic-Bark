from InputData import Environment
from Models import *

def process_input(file_path):
    file = open(file_path)
    header = file.readline()
    print("Processing " + file_path + " with header " + header)

    header_array = header.split()
    print(header_array)

    with open(file_path) as fp:
        for cnt, line in enumerate(fp):
            if cnt > int(header_array[2]):
                streets = line.split()
                streets.pop(0)
                print(streets)
        


    return Environment(header_array[0], header_array[1], header_array[2], header_array[3], header_array[4])
