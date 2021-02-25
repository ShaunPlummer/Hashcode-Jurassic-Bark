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
        self. duration = duration
        self.intersection = intersections
        self._streetList = streetList
        self._carList = carList
        self._bonus = bonusPoints
