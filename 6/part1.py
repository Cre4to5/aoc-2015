with open("./6/input.txt", "r") as file:
    lines = file.readlines()

    lights = [1_000*[False] for _ in range(1_000)]

    for line in lines:
        temp = line.split(" ")
        if temp[0] == "toggle":
            cord_index = 1
            decider = temp[0]
        else:
            cord_index = 2
            decider = temp[1]
        start_x, start_y = temp[cord_index].split(",")
        end_x, end_y = temp[cord_index + 2].split(",")
        start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(end_x), int(end_y)
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):   
                match decider:
                    case "toggle":
                        lights[x][y] = not lights[x][y]
                    case "on":
                        lights[x][y] = True
                    case "off":
                        lights[x][y] = False
        
    count = 0
    for i in range(0, 1_000):
        for j in range(0, 1_000):
            if lights[i][j]:
                count += 1
                print(1,end="")
            else: print(0,end="")
        print()
    print(count)