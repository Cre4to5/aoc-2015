import hashlib

with open("./4/input.txt", "r") as file:
    letters = file.read()
    potential = []
    for i in range(0 , 100_000):
        print(f"{i/1_000}%")
        minimum = "ffffffffffffffffffffffffffffffff"
        min_i = 0
        count = 0
        input1 = letters
        next = False
        for j in range(len(str(i)),5):
            input1 += "0"
        input1 += str(i)
        print(input1)
        hashed = hashlib.md5(input1.encode('utf-8')).hexdigest()
        print(hashed)
        if ("0x" + hashed) < ("0x" + minimum):
            count += 1
            minimum = hashed
            min_i = i
        for j in range(0,5):
            if hashed[j] != "0":
                next = True
                break
        if next:
            continue
        potential.append((hashed,i))
    print(potential)
    print(min_i,minimum, count)