# Input reading
line_of_text = input("Enter a line of text: ")

# Splitting the input line into words
words = line_of_text.split()

# Creating the dictionary
word_dict = {}

# Populating the dictionary
for word in words:
    first_char = word[0]
    if first_char in word_dict:
        word_dict[first_char].append(word)
    else:
        word_dict[first_char] = [word]

# Printing the dictionary
print("Dictionary with first character as key and words as values:")
print(word_dict)
