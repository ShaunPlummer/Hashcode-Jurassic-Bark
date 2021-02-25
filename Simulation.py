from InputData import Environment


class Simulation:
    def __init__(self, file_name, environment: Environment):
        self.file_name = file_name
        self.environment = environment

    def file_name(self):
        return self.file_name()

    def run(self):
        print("Running simulation")
        self.writeToFile()

    def writeToFile(self):
        baseline = 30

        with open("output/" + self.file_name, "w+") as file:
            # Print the total number of intersections
            intersections = self.environment.intersections
            file.write(str(len(intersections)) + "\n")
            # iterate the intersections
            for inter in intersections:
                # print("\n Intersection" + str(inter.num) + " in: " + str(inter.streets_in))
                # print the number of incoming streets

                traffic_count_all = sum(self.environment.streetList[s].traffic_count for s in inter.streets_in)

                file.write(str(inter.num) + "\n")
                file.write(str(len(inter.streets_in)) + "\n")
                # iterate the streets and
                for street_name in inter.streets_in:
                    street_model = self.environment.streetList[street_name]

                    traffic_count = self.environment.streetList[street_name].traffic_count

                    if traffic_count_all == 0:
                        time = 0
                    else:
                        time = int(traffic_count / traffic_count_all) * baseline

                    if time != 0:
                        file.write(street_model.name + " " + str(time) + " \n")
