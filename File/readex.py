#Reading from a Text File
#Objective: Show how to read content from a file.
#Outcome: Reads and prints the content of the file.

# Reading content from a file
with open("example1.txt", "r") as file:
    content = file.read()
    print(content)
print("Content read from example1.txt")