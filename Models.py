class Intersection:
    def __init__(self, num, streets_in, streets_out):
        self.num = num
        self.streets_in = streets_in
        self.streets_out = streets_out

    # def getMaxStreetWithMaxCars:
#         self.streets.


class Street:
    def __init__(self, line):
        parts = line.split(" ")
        self.start = parts[0]
        self.end = parts[1]
        self.name = parts[2]
        self.time = parts[3]


class Car:
    def __init__(self, id, num_of_streets, streets):
        self.id = id
        self.num_of_streets = num_of_streets
        self.streets = streets
