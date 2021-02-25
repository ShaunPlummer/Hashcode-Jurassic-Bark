from math import floor


class Intersection:
    def __init__(self, num, streets_in, streets_out):
        self.num = num
        self.streets_in = streets_in
        self.streets_out = streets_out


class Street:
    def __init__(self, line):
        parts = line.split(" ")
        self.start = int(parts[0])
        self.end = int(parts[1])
        self.name = parts[2]
        self.time = int(parts[3])
        self.traffic_count = 0

    def get_green_time(self):
        if self.traffic_count == 0:
            return 1
        else:
            time = floor(abs(self.time * (self.traffic_count / 100)))
            return max([time, self.time])

    def __str__(self):
        return str(self.start) + " -> " + str(self.end) + " " + self.name + str(self.time)


class Car:
    def __init__(self, id, num_of_streets, streets):
        self.id = id
        self.num_of_streets = num_of_streets
        self.streets = streets
