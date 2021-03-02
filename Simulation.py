from Environment import Environment
import math
from collections import deque
from collections import defaultdict


class Simulation:
    def __init__(self, file_name, environment: Environment):
        self.file_name = file_name
        self.environment = environment

    def file_name(self):
        return self.file_name()

    def run(self):
        self.solve()
        self.simulate()
        self.write_to_file()

    def set_green_duration(self, intersections, street, duration):
        value = min(street.time, int(duration))
        if value > 0:
            intersections[street.end].schedule.append((street.name, value))

    def simulate(self):
        print("Running simulation")
        duration = self.environment.duration
        bonus = self.environment.bonus
        streets = self.environment.streetList
        cars = self.environment.carList
        intersections = self.environment.intersections

        queues = {}  # Maps of street names to queues of cars enqueued at the end of that street
        arrivals = defaultdict(list)  # Mapping of time to car when the car will arrive at the end of its current street
        lights = defaultdict(list)  # Mapping of time to car when the intersection will advance to next green light in its schedule

        for s in streets:
            queues[s] = deque()

        # Initialise problem
        for c in cars:
            queues[c.streets[0]].appendleft(c)
        for i in intersections:
            if len(i.schedule) > 1:
                t_next_street = i.schedule[0][1]
                lights[t_next_street].append(i)

        t = 0
        score = 0

        while t <= duration:
            # print("--------------------")
            # print("t - " + str(t))
            if t in arrivals:
                for (car, i) in arrivals[t]:
                    if i == car.num_of_streets - 1:
                        # print("car arrived, early by " + str(duration - t))
                        score += bonus + duration - t
                    else:
                        queues[car.streets[i]].appendleft(car)
                        # print("car " + str(car.id) + " arrived at end of street " + car.streets[i])

            if t in lights:
                # print("lights scheduled to change at " + str(t))
                # print(lights[t])
                for intersection in lights[t]:
                    next_index = (intersection.green_street_index + 1) % len(intersection.schedule)
                    intersection.green_street_index = next_index
                    lights[t + intersection.schedule[next_index][1]].append(intersection)

            for (s, q) in queues.items():
                if q:
                    if intersections[streets[s].end].is_green(s):
                        # Green light
                        car = q.pop()
                        car.location += 1  # Car moves to next street
                        #print("car " + str(car.id) + " crossed intersection to street " + car.streets[car.location])
                        travel_time = streets[car.streets[car.location]].time  # next road travel time
                        if t + travel_time < duration:
                            arrivals[t + travel_time].append((car, car.location))
                    else:
                        car = q[-1]
                        #print("car " + str(car.id) + " waiting at " + car.streets[car.location] + " -> " + car.streets[car.location + 1])
            t += 1

        print("score: " + str(score) + "\n")
        #input("next")

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

            non_zero_intersections = sum((0 if len(i.schedule) == 0 else 1) for i in intersections)

            file.write(str(non_zero_intersections) + "\n")

            # iterate the intersections
            for inter in self.environment.intersections:
                # Check number of streets with non-zero durations
                non_zero_streets = len(inter.schedule)

                if non_zero_streets != 0:
                    file.write(str(inter.num) + "\n")  # intersection ID
                    file.write(str(non_zero_streets) + "\n")  # non zero streets

                    for (street_name, green_duration) in inter.schedule:
                        street_model = self.environment.streetList[street_name]

                        if green_duration != 0:
                            file.write(street_model.name + " " + str(green_duration) + "\n")
