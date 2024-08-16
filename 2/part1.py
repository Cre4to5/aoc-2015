with open("./2/input.txt", "r") as file:
    input = file.readlines()
    area_sum = 0
    for line in input:
        a, b, c = line.split("x")
        a, b, c = int(a), int(b), int(c)
        area = 0
        area = 2 * ( a * b + b * c + a * c)
        maximum = max(a,b,c)
        area+= a * b * c / maximum
        area_sum += area
    print(area_sum)
