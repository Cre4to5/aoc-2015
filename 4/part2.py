import hashlib

with open("./4/input.txt", "r") as file:
    letters = file.read()
    i = 1
    while True:
        input1 = letters + str(i)
        # print(input1)
        hashed = hashlib.md5(input1.encode('utf-8')).hexdigest()
        # print(hashed)

        if hashed.startswith("000000"):
            potential = (hashed, i)
            break
        # print(f"{i/1_000}%")
        i += 1
    print(potential)