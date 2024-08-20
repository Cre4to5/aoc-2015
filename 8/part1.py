with open("./8/input.txt", "r") as file:
    lines = file.readlines()
    code_chars = 0
    memo_chars = 0
    for line in lines:
        line = line.strip()
        print(line)
        code_chars += len(line)

        line = eval(line)
        print(line)
        memo_chars += len(line)
    
    print(code_chars-memo_chars)