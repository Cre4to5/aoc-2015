with open("./5/input.txt", "r") as file:
    lines = file.readlines()
    nice_count = 0
    nices = []
    for line in lines:
        line = line.strip()
        # print(line)
        seen = []
        seen2 = []
        
        for i in range(len(line) - 1):
            pair = line[i:i + 2]
            if pair in line[i + 2:]:
                has_repets = True
                break

        condition2 = False
        for i in range(0, len(line) - 2):
            if line[i] == line[i + 2]:
                condition2 = True
        
        if condition2 and has_repets:
            # print("yes")
            nices.append(line)
            nice_count += 1
    print(nices)
    print(nice_count)