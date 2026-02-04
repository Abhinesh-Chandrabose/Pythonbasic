#Appending to a File
#Objective: Illustrate how to append text to an existing file.
#Outcome: Adds new text to the end of the file.

# Appending text to a file
with open("example1.txt", "a") as file:
    file.write("\n Hi !! This is an appended line.")
print("Text appended to example1.txt")
