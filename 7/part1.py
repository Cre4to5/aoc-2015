def NOT(number):
    return ~number & 0xFFFF

def AND(a,b):
    return a & b & 0xFFFF

def OR(a,b):
    return a | b & 0xFFFF

def LSHIFT(a,b):
    return a << b & 0xFFFF

def RSHIFT(a,b):
    return a >> b & 0xFFFF
known = {}
commands = ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"]
tokens = []

def func(index):
    if tokens[index].isnumeric():
        return int(tokens[index])
    else:
        return known[tokens[index]]

with open("./7/input.txt", "r") as file:
    lines = file.readlines()

    

    i = -1
    while True:
        i += 1
        if i >= len(lines):
            i = 0
        if len(lines) == 0:
            break

        tokens = lines[i].split(" ")
        tokens[-1] = tokens[-1].strip()
        # print(i ,len(lines))
        
        j = -1
        while True:
            j += 1
            # print(j)
            if tokens[j]=="->":
                if tokens[0]=="NOT":
                    if tokens[1].isnumeric():
                        result = NOT(int(tokens[1]))
                    else:
                        result = NOT(known[tokens[1]])
                else:
                    a = func(0)
                    if tokens[1]!="->":
                        b = func(2)
                    else: result = a
                    match tokens[1]:
                        case "AND":
                            result = AND(a,b)
                        case "OR":
                            result = OR(a,b)
                        case "LSHIFT":
                            result = LSHIFT(a,b)
                        case "RSHIFT":
                            result = RSHIFT(a,b)
                        case _:
                            print(tokens)
                known[tokens[j + 1]] = result
                lines.pop(i)
            if not tokens[j].isnumeric() and not tokens[j] in commands:
                if not tokens[j] in known.keys():
                    break
    print(known["a"])