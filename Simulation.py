from Environment import Environment
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

    def set_green_duration(self, intersections, street, duration):
        value = min(street.time, int(duration))
        street.green_duration = value
        if value != 0:
            intersections[street.end].solution_non_zero_streets += 1

    def solve(self):
        intersections = self.environment.intersections
        streets = self.environment.streetList

        business_factor = 2.0  # The higher this value, the larger the increase in green duration for busier streets
        max_green_factor = 0.75  # Represents maximum green duration for the street (x * time) - must be 0 < x <= 1

        for inter in intersections:
            # Check number of streets with non-zero durations
            traffic_count_all = sum(streets[s].traffic_count for s in inter.streets_in)
            non_zero_streets = sum((0 if streets[s].traffic_count == 0 else 1) for s in inter.streets_in)

            if non_zero_streets != 0:
                baseline = float(non_zero_streets)

                for street_name in inter.streets_in:
                    street = streets[street_name]
                    traffic_count = street.traffic_count

                    if traffic_count == 0:
                        time = 0  # no traffic comes through this street - no green duration
                    else:
                        business_value = float(traffic_count) / float(traffic_count_all)
                        time = baseline * business_value.__pow__(business_factor)

                        # limit green time to be between 1 and max
                        time = min(float(street.time) * max_green_factor, time)
                        time = max(1.0, time)

                    # set green light duration for this street - automatically incrementing non zero streets for inter
                    self.set_green_duration(intersections, street, time)

    def write_to_file(self):
        with open("output/" + self.file_name, "w+") as file:
            # The total number of intersections with at least one non-zero green_duration
            intersections = self.environment.intersections

            non_zero_intersections = sum((0 if i.solution_non_zero_streets == 0 else 1) for i in intersections)

            file.write(str(non_zero_intersections) + "\n")

            # iterate the intersections
            for inter in self.environment.intersections:
                # Check number of streets with non-zero durations
                non_zero_streets = inter.solution_non_zero_streets

                if non_zero_streets != 0:
                    file.write(str(inter.num) + "\n")  # intersection ID
                    file.write(str(non_zero_streets) + "\n")  # non zero streets

                    for street_name in inter.streets_in:
                        street_model = self.environment.streetList[street_name]

                        if street_model.green_duration != 0:
                            file.write(street_model.name + " " + str(street_model.green_duration) + "\n")

