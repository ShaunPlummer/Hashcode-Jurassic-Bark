from Environment import Environment
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

    streets = {}
    print("Processing " + file_path + " with header " + header)
    for i in range(0, street_count):
        # streets.append(Street(file.readline()))
        s = Street(file.readline())
        streets[s.name] = s

    print("streets" + str(len(streets)))

    intersections = []
    for i in range(0, intersection_count):
        intersections.append(Intersection(i, [], []))

    for key, street in streets.items():
        intersections[street.start].streets_out.append(street.name)
        intersections[street.end].streets_in.append(street.name)

    cars = []
    for i in range(0, car_count):
        line = file.readline()
        route = line.split()
        num = route.pop(0)
        car = Car(i, int(num), route)
        cars.append(car)

        for road in car.streets:
            streets[road].traffic_count += 1

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
