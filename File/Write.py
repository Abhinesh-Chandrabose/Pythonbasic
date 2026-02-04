#Writing to a Text File
#Objective: Demonstrate how to write text to a file using a context manager.
#Outcome: Creates a file and writes a line of text to it.

# Using context manager to write to a file
with open("example1.txt", "w") as file:
    file.write("Hello, this is a simple file write example.")
print("Text written to example1.txt")
