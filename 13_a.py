# Input the two strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Split the strings into words
words1 = string1.split()
words2 = string2.split()

# Create a dictionary to count occurrences of each word
word_count = {}

# Count words in the first string
for word in words1:
    word_count[word] = word_count.get(word, 0) + 1

# Count words in the second string
for word in words2:
    word_count[word] = word_count.get(word, 0) + 1

# Find uncommon words
uncommon_words = [word for word in word_count if word_count[word] == 1]

# Display the result
print("Uncommon words:", uncommon_words)
