
class Intersection:
    def __init__(self, num, street):
        self.__num = num
        self.__steets = street

class Street:

    def __init__(self, name, start, end, time):
        self.name = name
        self.start = start
        self.end = end
        self.time = time

    def __init__(self, line):
        parts = line.split(" ")
        self.start = parts[0]
        self.end = parts[1]
        self.name = parts[2]
        self.time = parts[3]



