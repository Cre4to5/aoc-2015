from itertools import permutations as perm

with open("./9/input.txt", "r") as file:
    lines = file.readlines()

    cities = set()
    distances = {}
    
    for line in lines:
        line = line.split(" ")
        cities.add(line[0])
        cities.add(line[2])
        distances[f"{line[0]}-{line[2]}"] = int(line[4])
        distances[f"{line[2]}-{line[0]}"] = distances[f"{line[0]}-{line[2]}"]
    

    permutations = list(perm(cities))
    paths_distances = [0] * len(permutations)

    # print(cities)
    # print(distances)
    # print(paths)
    
    for i, path in enumerate(permutations):
        for j in range(0, len(path)-1):
            # print(j)
            try:
                add = distances[f"{path[j]}-{path[j + 1]}"]
            except:
                paths_distances[i] = float("inf")
                break
            else:
                paths_distances[i] += add
    
    print(min(paths_distances))