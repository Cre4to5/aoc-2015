with open("./3/input.txt", "r") as file:
    input = file.read()
    x , y = 0, 0
    visited = set()
    for char in input:
        # print(char)
        # print(x , y)
        visited.add((x,y))
        match char:
            case "^":
                y += 1
            case ">":
                x += 1
            case "v":
                y -= 1
            case "<":
                x -= 1
    print(len(visited))