class Environment:
    def __init__(
            self,
            duration,
            intersections,
            numStreet,
            numCars,
            bonusPoints,
            streetList,
            carList,
    ):
        self.duration = duration
        self.intersections = intersections
        self.numStreet = numStreet,
        self.numCars = numCars,
        self.streetList = streetList
        self.carList = carList
        self.bonus = bonusPoints

    def summary(self):
        print("car_count: " + str(len(self.carList)) + " \nstreet_count: " + str(
            len(self.streetList)) + "\nintersections: " + str(len(self.intersections)))
