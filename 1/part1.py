with open("./1/input.txt", "r") as file:
    input = file.read()
    level = 0
    for i, perentesis in enumerate(input):
        if(perentesis=="("): level+=1
        if(perentesis==")"): level-=1
    print(level)