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

    def getStreet(self, search_name):
        for s in self.streetList:
            if s.name == search_name:
                return s

    def summary(self):
        print("car_count: " + str(len(self.carList)) + " \nstreet_count: " + str(
            len(self.streetList)) + "\nintersections: " + str(len(self.intersections)))
