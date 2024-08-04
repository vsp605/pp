input_string = input("Enter a string: ")
alphanumeric_string = ''.join(char for char in input_string if char.isalnum())
print("Alphanumeric string:", alphanumeric_string)
