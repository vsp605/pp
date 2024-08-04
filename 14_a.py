# Input the string
input_string = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Remove vowels from the string
result_string = ''.join([char for char in input_string if char not in vowels])

# Display the result
print("String after removing vowels:", result_string)
