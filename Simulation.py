from InputData import Environment
import math

class Simulation:
    def __init__(self, file_name, environment: Environment):
        self.file_name = file_name
        self.environment = environment

    def file_name(self):
        return self.file_name()

    def run(self):
        print("Running simulation")
        self.solve()
        self.write_to_file()

    def set_green_duration(self, street, duration):
        value = min(street.time, int(duration))
        street.green_duration = value
        if value != 0:
            self.environment.intersections[street.end].non_zero_streets += 1

    def solve(self):
        intersections = self.environment.intersections

        baseline = 20.0

        for inter in intersections:
            # Check number of streets with non-zero durations
            traffic_count_all = sum(self.environment.streetList[s].traffic_count for s in inter.streets_in)

            for street_name in inter.streets_in:
                street_model = self.environment.streetList[street_name]
                traffic_count = street_model.traffic_count

                if traffic_count_all == 0:
                    time = 0
                else:
                    time = math.ceil((float(traffic_count) / float(traffic_count_all)) * baseline)
                time = min(street_model.time, time)

                self.set_green_duration(street_model, time)

    def write_to_file(self):
        with open("output/" + self.file_name, "w+") as file:
            # The total number of intersections with at least one non-zero green_duration

            non_zero_intersections = sum((0 if i.non_zero_streets == 0 else 1) for i in self.environment.intersections)

            file.write(str(non_zero_intersections) + "\n")

            # iterate the intersections

            for inter in self.environment.intersections:
                # Check number of streets with non-zero durations
                non_zero_streets = sum((0 if self.environment.streetList[s].green_duration == 0 else 1) for s in inter.streets_in)

                if non_zero_streets != 0:
                    file.write(str(inter.num) + "\n")  # intersection ID
                    file.write(str(non_zero_streets) + "\n")

                    for street_name in inter.streets_in:
                        street_model = self.environment.streetList[street_name]

                        if street_model.green_duration != 0:
                            file.write(street_model.name + " " + str(street_model.green_duration) + "\n")

