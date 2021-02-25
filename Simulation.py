from InputData import Environment


class Simulation:
    def __init__(self, file_name, environment: Environment):
        self.file_name = file_name
        self.environment = environment

    def file_name(self):
        return self.file_name()

    def run(self):
        print("Running simulation")

        for int in self.environment.intersection:
            int.getMaxStreetWithMaxCars()




