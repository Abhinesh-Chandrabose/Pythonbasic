# Create a script that takes a sentence as input and uses a dictionary to count the frequency of each word. The output should be the word and its count.
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = {} # Initialize an empty dictionary to store word counts
for word in words:
    word_count[word] = word_count.get(word, 0) + 1 # Count the occurrences of each word
for word, count in word_count.items(): # Print the word counts
    print(f"{word}: {count}") #
