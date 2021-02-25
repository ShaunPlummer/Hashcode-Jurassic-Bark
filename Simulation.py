from InputData import Environment


class Simulation:
    def __init__(self, file_name, environment: Environment):
        self.file_name = file_name
        self.environment = environment

    def file_name(self):
        return self.file_name()

    def run(self):
        print("Running simulation")

    def writeToFile(self):
        with open("output" + self.file_name(), "a") as file:
            # Print the total number of intersections
            file.write(str(len(self.environment.intersections)))

            # iterate the intersections
            for inter in self.environment.intersections:
                # print the number of incomming streets
                file.write(str(len(inter.street_in)))
                # iterate the streets and print their time
                for street in inter.street_in:
                    file.write(str(street.time))

        file.close()
