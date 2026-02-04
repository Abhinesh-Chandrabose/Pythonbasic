#Using 'try-except' for File Not Found
#Objective: Handle file not found error using exception handling.
#Outcome: Prints an error message if the file does not exist.

# Handle file not found error
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")