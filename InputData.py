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
        self.intersection = intersections
        self.streetList = streetList
        self.carList = carList
        self.bonus = bonusPoints

    def summary(self):
        print("car_count" + str(len(self.carList)) + " \n street_count" + str(len(self.streetList)))
