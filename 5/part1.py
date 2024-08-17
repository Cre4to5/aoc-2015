with open("./5/input.txt", "r") as file:
    lines = file.readlines()
    nice_count = 0
    nices = []
    vowels = ["a","e","i","o","u"]
    for line in lines:
        line = line.strip()
        # print(line)
        if any(bad in line for bad in ["ab", "cd", "pq", "xy"]):
            # print("has bad")
            continue
        vowels_count = 0
        doubles = False

        previous_letter = ""
        for letter in line:
            if letter in vowels:
                vowels_count += 1
                # print(f"vowel: {letter}")

            if letter == previous_letter:
                doubles = True
                # print("has doubles")
            previous_letter = letter
        
        if vowels_count >= 3 and doubles:
            nice_count += 1
            nices.append(line)
    print(nices)
    print(nice_count)