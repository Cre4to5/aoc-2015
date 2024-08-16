with open("./3/input.txt", "r") as file:
    input = file.read()
    x , y = 0, 0
    x_r, y_r = 0, 0
    visited = set()
    for i, char in enumerate(input):
        # print(char)
        # print(x , y)
        visited.add((x,y))
        visited.add((x_r,y_r))
        if i % 2 == 0:
            match char:
                case "^":
                    y += 1
                case ">":
                    x += 1
                case "v":
                    y -= 1
                case "<":
                    x -= 1
        else:
            match char:
                case "^":
                    y_r += 1
                case ">":
                    x_r += 1
                case "v":
                    y_r -= 1
                case "<":
                    x_r -= 1
    print(len(visited))