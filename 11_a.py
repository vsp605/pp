# Read the input string
s = input("Enter a string: ")

# Check if the string is a palindrome
is_palindrome = s == s[::-1]

# Check if the string is symmetrical
length = len(s)
is_symmetrical = False
if length % 2 == 0:
    mid = length // 2
    if s[:mid] == s[mid:][::-1]:
        is_symmetrical = True

# Print results
if is_palindrome:
    print(f"'{s}' is a palindrome.")
else:
    print(f"'{s}' is not a palindrome.")

if is_symmetrical:
    print(f"'{s}' is symmetrical.")
else:
    print(f"'{s}' is not symmetrical.")
