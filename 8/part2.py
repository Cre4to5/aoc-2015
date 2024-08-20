with open("./8/input.txt", "r") as file:
    lines = file.readlines()
    code_chars = 0
    memo_chars = 0
    for line in lines:
        line = line.strip()
        print(line)
        code_chars += len(line)

        new_line="\""
        for char in line:
            if char == "\\" or char == "\"":
                new_line += "\\"
            new_line += char
        new_line += "\""

        print(new_line)
        memo_chars += len(new_line)
    
    print(memo_chars - code_chars)