import math

with open("./9/input.txt", "r") as file:
    lines = file.readlines()

    cities = set()
    distances = {}
    
    for line in lines:
        line = line.split(" ")
        cities.add(line[0])
        cities.add(line[2])
        distances[f"{line[0]}-{line[2]}"] = int(line[4])
        distances[f"{line[2]}-{line[0]}"] = int(line[4])
    

    #TODO: better way for all permutations
    for i in range(0,math.factorial(len(cities))):
        cities_copy = cities
        i = -1
        while True:
            i += 1
            cities_copy