import re

# Input reading
ifsc_code = input("Enter the IFSC code to validate: ")

# Regular expression for a valid IFSC code
pattern = r'^[A-Za-z]{4}0[A-Za-z0-9]{6}$'

# Matching the IFSC code with the pattern
if re.match(pattern, ifsc_code):
    print(f"{ifsc_code} is a valid IFSC code.")
else:
    print(f"{ifsc_code} is not a valid IFSC code.")
