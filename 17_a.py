# Input string
s = "aabccba"

# Initialize an empty result string
result = ""

# Iterate through the string
for i in range(len(s)):
    # Add the character to the result if it's the first character or different from the previous one
    if i == 0 or s[i] != s[i - 1]:
        result += s[i]

print("Original String:", s)
print("String after removing consecutive duplicates:", result)
