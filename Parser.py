from InputData import Environment
from Models import *


def process_input(file_path):
    file = open(file_path)
    header = file.readline()

    parts = header.split(" ")
    rounds = int(parts[0])
    intersection_count = int(parts[1])
    street_count = int(parts[2])
    car_count = int(parts[3])
    bonus = int(parts[4])

    streets = []

    print("Processing " + file_path + " with header " + header)
    for i in range(0, street_count):
        streets.append(Street(file.readline()))

    print("generate intersections from streets here")
    intersections = []

    cars = []
    for i in range(0, car_count):
        line = file.readline()
        streets = line.split()
        num = streets.pop(0)
        car = Car(i, num, streets)
        cars.append(car)

    file.close()
    return Environment(
        rounds,
        intersections,
        street_count,
        car_count,
        bonus,
        streets,
        cars
    )
