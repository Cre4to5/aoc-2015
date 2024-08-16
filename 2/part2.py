with open("./2/input.txt", "r") as file:
    input = file.readlines()
    ribbbon_sum = 0
    for line in input:
        a, b, c = line.split("x")
        a, b, c = int(a), int(b), int(c)
        maximum = max(a,b,c)
        ribbon = a * b * c + 2 * (a + b + c - maximum)
        ribbbon_sum+=ribbon
    print(ribbbon_sum)
