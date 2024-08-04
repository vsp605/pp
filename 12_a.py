# Input the string
input_string = input("Enter a string: ")

# Calculate the midpoint
midpoint = len(input_string) // 2

# Convert the first half to uppercase
first_half_upper = input_string[:midpoint].upper()

# Combine the uppercase first half with the second half
result_string = first_half_upper + input_string[midpoint:]

# Print the result
print("Resulting string:", result_string)
