class Environment:
    def __init__(
            self,
            duration,
            intersections,
            num_streets,
            num_cars,
            bonus_points,
            street_list,
            car_list,
    ):
        self.duration = duration
        self.intersections = intersections
        self.numStreet = num_streets,
        self.numCars = num_cars,
        self.streetList = street_list
        self.carList = car_list
        self.bonus = bonus_points

    def summary(self):
        print("car_count: " + str(len(self.carList)) + " \nstreet_count: " + str(
            len(self.streetList)) + "\nintersections: " + str(len(self.intersections)))
