#Reading Line by Line
#Objective: Demonstrate reading a file line by line.
#Outcome: Prints each line of the file separately.

# Reading file line by line
with open("example1.txt", "r") as file:
    for line in file:
        print(line.strip())
print("Finished reading example1.txt")