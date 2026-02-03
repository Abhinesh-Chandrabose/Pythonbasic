with open("data.txt", "r") as file:
    i=1
    for line in file.readlines():
        print(f"{i}: {line.strip()}")
        i += 1
