with open("./5/input.txt", "r") as file:
    lines = file.readlines()
    nice_count = 0
    nices = []
    for line in lines:
        line = line.strip()
        condition2 = False
        print(line)
        seen = []
        seen2 = []
        for i in range(1, len(line) - 2, 2):
            seen2.append(f"{line[i]}{line[i + 1]}")
        for i in range(0, len(line) - 1, 2):
            seen.append(f"{line[i]}{line[i + 1]}")
        has_repets = len(set(seen)) != len(seen) or len(set(seen2)) != len(seen2)

        for i in range(0, len(line) - 2):
            if line[i] == line[i + 2]:
                condition2 =True
        
        if condition2 and has_repets:
            print("yes")
            nices.append(line)
            nice_count += 1
    print(nices)
    print(nice_count)