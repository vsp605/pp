# Input string and number of rotations
s = "GeeksforGeeks"
d = 2

# Length of the string
n = len(s)

# Clockwise rotation
clockwise_rotated = s[-d:] + s[:-d]
print("Clockwise Rotation:", clockwise_rotated)

# Anticlockwise rotation
anticlockwise_rotated = s[d:] + s[:d]
print("Anticlockwise Rotation:", anticlockwise_rotated)
