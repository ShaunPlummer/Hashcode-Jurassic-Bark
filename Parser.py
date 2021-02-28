from Environment import Environment
from Models import *


def process_input(file_path):
    file = open(file_path)
    header = file.readline()

    parts = header.split(" ")
    duration = int(parts[0])
    intersection_count = int(parts[1])
    street_count = int(parts[2])
    car_count = int(parts[3])
    fixed_award = int(parts[4])

    impossible_routes = 0

    streets = {}
    perfect_score = 0
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
        total_car_score = 0
        line = file.readline()
        route = line.split()
        num = route.pop(0)
        car = Car(i, num, route)
        cars.append(car)

        route_length = 0
        for road in car.streets:
            streets[road].traffic_count += 1
            route_length += streets[road].time
        if route_length > duration:
            impossible_routes += 1
        else:
            total_car_score += fixed_award + (duration - route_length)
        perfect_score += total_car_score

    file.close()

    print("")
    print("Input analysis for " + file_path)
    print("Impossible routes: " + str(impossible_routes))
    print("Perfect score: " + str(perfect_score))
    print("")

    return Environment(
        duration,
        intersections,
        street_count,
        car_count,
        fixed_award,
        streets,
        cars
    )
