import hashlib

def min_hex(a, b):
    # Normalize the case to ensure consistent comparison
    a = a.lower()
    b = b.lower()
    
    # Compare by length first
    if len(a) > len(b):
        return b
    if len(a) < len(b):
        return a
    
    # Compare digit by digit if lengths are equal
    for i in range(len(a)):
        if int(a[i], 16) < int(b[i], 16):
            return a
        if int(a[i], 16) > int(b[i], 16):
            return b
    
    # If all digits are equal, return either
    return a  # or return b; they are equal

with open("./4/input.txt", "r") as file:
    letters = file.read()
    potential = []
    minimum = "ffffffffffffffffffffffffffffffff"
    min_i = 0

    for i in range(100_000):
        # Construct the input string by padding i to ensure a fixed length (e.g., 5 digits)
        input1 = letters + str(i).zfill(5)

        # Generate the MD5 hash of the input string
        hashed = hashlib.md5(input1.encode('utf-8')).hexdigest()

        # Compare the current hash with the minimum
        if min_hex(minimum, hashed) == hashed:
            minimum = hashed
            min_i = i

        # Check if the first five characters are zeros
        if hashed.startswith("00000"):
            potential.append((hashed, i))

        # Progress tracking (remove or comment out for final use)
        if i % 1000 == 0:
            print(f"Progress: {i/1000}%")

    # Output the results
    print("Potential hashes:", potential)
    print(f"Smallest hash found: {minimum} with i={min_i}")