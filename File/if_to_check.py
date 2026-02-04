#Using 'if' to Check File Content
#Objective: Use conditional logic to check for a word in the file.
#Outcome: Prints a message if the word is found.

# Check if a specific word exists in the file
with open("example1.txt", "r") as file:
    content = file.read()
    count = content.count("appended")
    if count > 0:
        print(f"The word 'appended' was found {count} times.")
    else:
        print("The word 'appended' was not found.")
print("Finished checking example1.txt")