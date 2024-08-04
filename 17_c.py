# Input binary tuple
binary_tuple = (1, 0, 1, 1)

# Initialize the result
result = 0

# Iterate over the tuple
for i in range(len(binary_tuple)):
    # Calculate the power of 2 for the current position
    power = len(binary_tuple) - i - 1
    # Add the corresponding value to the result
    result += binary_tuple[i] * (2 ** power)

print("Binary Tuple:", binary_tuple)
print("Integer Value:", result)
