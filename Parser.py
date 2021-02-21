from InputData import Environment


def process_input(file_path):
    file = open(file_path)

    header = file.readline()
    print("Processing " + file_path + " with header " + header)

    return Environment(0, 0, 0)
