import os

from Parser import process_input
from Simulation import Simulation

if __name__ == '__main__':
    print("Starting")
    input_dir = "input"

    directory = os.fsencode(input_dir)
    for file in os.listdir(directory):
        file_name = os.fsdecode(file)
        if file_name.endswith(".txt"):
            environment = process_input(input_dir + "/" + file_name)
            environment.summary()
            Simulation(file_name, environment).run()
            continue
        else:
            continue
